#!/usr/bin/python3
#
# Calculate identifiable objects, non-identifiable groups, each group has at
# least 1 object.
#
# This is like N books divided into M groups.


import argparse

# Key is (n, k) tuple, value is the corresponding stirling second kind number.
TABLE = {}

def StirlingSecondKind(num_objects, num_groups):
  if num_objects == num_groups:
    return 1

  if num_groups == 1:
    return 1

  if (num_objects, num_groups) in TABLE:
    return TABLE[(num_objects, num_groups)]

  result = StirlingSecondKind(num_objects-1, num_groups-1) + \
           num_groups * StirlingSecondKind(num_objects-1, num_groups)
  TABLE[(num_objects, num_groups)] = result
  return result

def main():
  parser = argparse.ArgumentParser(usage=__doc__)

  parser.add_argument('num_objects', type=int, default=5,
                      help='Number of objects to assign to groups.')

  parser.add_argument('num_groups', type=int, default=2,
                      help='Number of groups to receive to objects.')

  FLAGS = parser.parse_args()
  print(f'Number of objects: {FLAGS.num_objects}')
  print(f'Number of groups: {FLAGS.num_groups}')

  print(f'There are {len(TABLE)} intermediate result.')
  for key in TABLE:
    print(f'\tS({key[0], key[1]}) = {TABLE[key]}')

  print(StirlingSecondKind(FLAGS.num_objects, FLAGS.num_groups))


if __name__=='__main__':
  main()
