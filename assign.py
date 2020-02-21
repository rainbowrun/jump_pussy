#!/usr/bin/python3
#
# A program to verify combinatronics assign problem by enumeration.


import argparse
import copy
import math
import sys

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


class Solution:
  def __init__(self, num_groups):
    # Groups in the solution.
    self.groups = []
    for _ in range(num_groups):
      self.groups.append([])

    # Flag used in dedup stage.
    self.is_duplicate = True

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
        new_solution.groups[group_index].append(object)
        new_solutions.append(new_solution)

    solutions = new_solutions

  # Verify the result.
  for solution in solutions:
    assert len(solution.groups) == FLAGS.num_groups
  return solutions


def DedupIdentifiableGroups(solutions):
  return solutions


def DedupNonIdentifiableGroups(solutions):
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

if FLAGS.group_identifiable:
  solutions = DedupIdentifiableGroups(solutions)
else:
  solutions = DedupNonIdentifiableGroups(solutions)

for solution in solutions:
  print(f'\t{solution}')
print(f'Number of different solutions: {len(solutions)}')
