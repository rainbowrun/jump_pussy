#!/usr/bin/python3

"""
A program solves combinatorics assign problems by enumerating all the
possible solutions and filtering.
"""

import argparse
import functools
import math


class Solution:
  def __init__(self, num_groups):
    # Groups in the solution.
    self.groups = []
    for _ in range(num_groups):
      self.groups.append([])

    # Flag used in dedup stage.
    self.is_duplicate = False

  def __str__(self):
    return f'{self.groups}'


def RecursiveLoop(num_groups, level, group_index_list, objects, solutions):
  level = level - 1

  for i in range(num_groups):
    group_index_list.append(i)

    if level != 0:
      RecursiveLoop(num_groups, level, group_index_list, objects, solutions)
    else:
      solution = Solution(num_groups)
      for object_index, group_index in enumerate(group_index_list):
        solution.groups[group_index].append(objects[object_index])
      solutions.append(solution)
      if len(solutions) % 1_000_000 == 0:
        print(f'{len(solutions)} solutions are created.')

    group_index_list.pop()


def CreateCandidateSolutionsByRecursive(objects, num_groups):
  solutions = []
  RecursiveLoop(num_groups, len(objects), [], objects, solutions)
  return solutions


def CreateCandidateSolutionsByNumberEncoding(objects, num_groups):
  # Each number in (num_groups ^ num_objects) is a solution.
  # Here the number is treated as an encoding of the groups.
  num_objects = len(objects)

  solutions = []
  for i in range(int(math.pow(num_groups, num_objects))):
    solution = Solution(num_groups)

    for object_index in range(num_objects):
      a = i // num_groups
      b = i % num_groups
      solution.groups[b].append(objects[object_index])
      i = a

    solutions.append(solution)

  return solutions


def DedupIdentifiableGroups(solutions):
  # The best duplicate method is to sort all the solutions, and process them in
  # one pass, which is n*log(n).

  # To compare two solution, we first compare the size of corresponding groups,
  # solution with smaller groups go first. If all the group sizes are equal, the
  # content of the group is compared, group with smaller elements go first.
  def compare_solution(solution_a, solution_b):
    for group_a, group_b in zip(solution_a.groups, solution_b.groups):
      if len(group_a) < len(group_b):
        return -1
      if len(group_a) > len(group_b):
        return 1

    for group_a, group_b in zip(solution_a.groups, solution_b.groups):
      for element_a, element_b in zip(group_a, group_b):
        if element_a < element_b:
          return -1
        if element_a > element_b:
          return 1

    return 0

  solutions.sort(key=functools.cmp_to_key(compare_solution))

  current_solution = solutions[0]
  for solution in solutions[1:]:
    if compare_solution(current_solution, solution) == 0:
      solution.is_duplicate = True
    else:
      current_solution = solution

  return [solution for solution in solutions if not solution.is_duplicate]


def DedupNonIdentifiableGroups(solutions):
  # For non-identifiable groups, we need to sort the groups of a solution then
  # to compare every group along the index to decide if two solutions are the
  # same. Sort the groups by:
  #     - First by group size, small groups go first.
  #     - Second by element: groups with the same size compared by
  #       their elements. Smaller elements go first.

  # A comparison function is any callable that accept two arguments, compares
  # them, and returns a negative number for less-than, zero for equality, or a
  # positive number for greater-than.
  def compare_group(group_a, group_b):
    if len(group_a) < len(group_b):
      return -1
    if len(group_a) > len(group_b):
      return 1

    for element_a, element_b in zip(group_a, group_b):
      if element_a < element_b:
        return -1
      if element_a > element_b:
        return 1

    return 0

  for solution in solutions:
    solution.groups.sort(key=functools.cmp_to_key(compare_group))

  return DedupIdentifiableGroups(solutions)


def add_bool_arg(parser, name, default, help):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true', help=help)
    group.add_argument('--no-' + name, dest=name, action='store_false', help=help)
    parser.set_defaults(**{name:default})


def main():
  parser = argparse.ArgumentParser(usage=__doc__)

  parser.add_argument('num_objects', type=int, default=5,
                      help='Number of objects to assign to groups.')

  parser.add_argument('num_groups', type=int, default=2,
                      help='Number of groups to receive to objects.')

  add_bool_arg(parser,
               name='object_identifiable',
               default=False,
               help="Whether the objects are identifiable.")

  add_bool_arg(parser,
               name='group_identifiable',
               default=False,
               help="Whether the groups are identifiable.")

  add_bool_arg(parser,
               name='allow_empty_group',
               default=False,
               help="Whether empty groups are allowed.")

  add_bool_arg(parser,
               name='print_candidate_groups',
               default=False,
               help="Whether to print canidate groups.")

  add_bool_arg(parser,
               name='print_final_groups',
               default=False,
               help="Whether to print final groups.")

  FLAGS = parser.parse_args()
  print(f'Number of objects: {FLAGS.num_objects}')
  print(f'Number of groups: {FLAGS.num_groups}')
  print(f'Objects are identifiable: {FLAGS.object_identifiable}')
  print(f'Groups are identifiable: {FLAGS.group_identifiable}')
  print(f'Allow empty group: {FLAGS.allow_empty_group}')

  if FLAGS.object_identifiable:
    objects = list(range(FLAGS.num_objects))
  else:
    objects = [0] * FLAGS.num_objects
  print(f'Objects: {objects}')

  # Create candidate solutions.
  solutions = CreateCandidateSolutionsByRecursive(objects, FLAGS.num_groups)

  # Verify the result.
  assert len(solutions) == math.pow(FLAGS.num_groups, FLAGS.num_objects)
  for solution in solutions:
    assert len(solution.groups) == FLAGS.num_groups

  if FLAGS.print_candidate_groups:
    for solution in solutions:
      print(f'\t{solution}')
  print(f'Number of candidate solutions: {len(solutions)}')

  # Filter empty groups if necessary.
  if not FLAGS.allow_empty_group:
    no_empty_group_solutions = []
    for solution in solutions:
      if all([len(group) != 0 for group in solution.groups]):
        no_empty_group_solutions.append(solution)
    print(f'{len(solutions)-len(no_empty_group_solutions)}'
          f' empty groups are filtered.')
    solutions = no_empty_group_solutions

  # Sort all the groups.
  print(f'{len(solutions)} solutions are left.')
  for solution in solutions:
    for group in solution.groups:
      group.sort()

  if FLAGS.group_identifiable:
    solutions = DedupIdentifiableGroups(solutions)
  else:
    solutions = DedupNonIdentifiableGroups(solutions)

  if FLAGS.print_final_groups:
    for solution in solutions:
      print(f'\t{solution}')
  print(f'Number of final solutions: {len(solutions)}')


if __name__ == '__main__':
  main()
