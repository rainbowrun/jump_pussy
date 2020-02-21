#!/usr/bin/python3

"""
A program solves combinatorics assign problems by enumerating all the
possible solutions and then filtering.
"""

import argparse
import copy
import itertools
import functools

parser = argparse.ArgumentParser(usage=__doc__)

parser.add_argument('num_objects', type=int, default=5,
                    help='Number of objects to assign to groups.')

parser.add_argument('num_groups', type=int, default=2,
                    help='Number of groups to receive to objects.')

parser.add_argument('--object_identifiable',
                    action='store_true',
                    default=False,
                    help="Whether the objects are identifiable.")

parser.add_argument('--group_identifiable',
                    action='store_true',
                    default=False,
                    help="Whether the groups are identifiable.")

parser.add_argument('--allow_empty_group',
                    action='store_true',
                    default=False,
                    help="Whether empty groups are allowed.")


class Solution:
  def __init__(self, num_groups):
    # Groups in the solution.
    self.groups = []
    for _ in range(num_groups):
      self.groups.append(set())

    # Flag used in dedup stage.
    self.is_duplicate = False

  def __str__(self):
    return f'{self.groups}'


def CreateCandidateSolutions(objects, num_groups):
  # Start with 'num_groups' of empty groups as the initial solution.
  start_solution = Solution(num_groups)
  solutions = [start_solution]

  for object in objects:
    print(f'Consider object: {object}')
    new_solutions = []

    # For each object, num_groups new grouping solutions are created.
    for solution in solutions:
      for group_index in range(len(solution.groups)):
        new_solution = copy.deepcopy(solution)
        new_solution.groups[group_index].add(object)
        new_solutions.append(new_solution)

    solutions = new_solutions

  # Verify the result.
  for solution in solutions:
    assert len(solution.groups) == FLAGS.num_groups
  return solutions


def DedupIdentifiableGroups(solutions):
  # For identifiable groups, group index (i.e. 0, 1, 2, ..., num_groups-1)
  # serves as group name, so we just need to compare groups of two solutions
  # one by one.
  for solution_a, solution_b in itertools.combinations(solutions, 2):
    if solution_a.is_duplicate or solution_b.is_duplicate:
      continue

    assert len(solution_a.groups) == len(solution_b.groups)
    
    if all([solution_a.groups[i] == solution_b.groups[i] for i in range(len(solution_a.groups))]):
      solution_b.is_duplicate = True
      
  return [solution for solution in solutions if not solution.is_duplicate]


def DedupNonIdentifiableGroups(solutions):
  # For non-identifiable groups, we need to sort the groups of a solution then
  # to compare every group along the index to decide if two solutions are the
  # same.
  #
  # Sort the groups by:
  #     - First by group size, small groups go first.
  #     - Second by element: groups with the same size compared by 
  #       their elements. Smaller elements go first.

  # A comparison function is any callable that accept two arguments, compares
  # them, and returns a negative number for less-than, zero for equality, or a
  # positive number for greater-than.
  def compare_group(group_a, group_b):
    if len(group_a)

  # TODO: Implement this.
  return solutions


FLAGS = parser.parse_args()
print(f'Number of objects: {FLAGS.num_objects}')
print(f'Number of groups: {FLAGS.num_groups}')
print(f'Objects are identifiable: {FLAGS.object_identifiable}')
print(f'Groups are identifiable: {FLAGS.group_identifiable}')

if FLAGS.object_identifiable:
  objects = list(range(FLAGS.num_objects))
else:
  objects = [0] * FLAGS.num_objects
print(f'Objects: {objects}')


# Create candidate solutions.
solutions = CreateCandidateSolutions(objects, FLAGS.num_groups)

# Filter empty groups if necessary.
if not FLAGS.allow_empty_group:
  no_empty_group_solutions = []
  for solution in solutions:
    if all([len(group) != 0 for group in solution.groups]):
      no_empty_group_solutions.append(solution)
  solutions = no_empty_group_solutions

if FLAGS.group_identifiable:
  solutions = DedupIdentifiableGroups(solutions)
else:
  solutions = DedupNonIdentifiableGroups(solutions)

for solution in solutions:
  print(f'\t{solution}')
print(f'Number of different solutions: {len(solutions)}')
