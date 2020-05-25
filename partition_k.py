#!/usr/bin/python3
#
# Partition number with k groups.
# See https://zhangxiaopan.net/?p=4866

import sys

# Key is (n, k) tuple, value is the corresponding number.
# n: number
# k: the number of groups
TABLE = {}


def partition_k(number, group):
  if (number, group) in TABLE:
    return TABLE[(number, group)]

  if group == 1:
    result = 1

  elif number == group:
    result = 1

  elif number < group:
    result = 0

  else:
    result = partition_k(number-1, group-1) + partition_k(number-group, group)

  TABLE[(number, group)] = result
  print(f'number: {number}, group: {group}, result: {result}')
  return result


def main():
  if len(sys.argv) !=3:
    print(f'Usage: {sys.argv[0]} <number> <group>')
    return

  number = int(sys.argv[1])
  group = int(sys.argv[2])

  result = partition_k(number, group)
  print(result)


if __name__=='__main__':
  main()
