#!/usr/bin/python3
"""Find an expression to use source numbers to get a target number.

For example:
  $ eval.py 5 6 7 8 24
    (5 + 7) * (8 - 6) = 24

  $ eval.py 5 2 7
    (5 + 2) = 7
"""

import argparse
import itertools
import math
import sys

parser = argparse.ArgumentParser(usage=__doc__)

#
# 6 - (7! / (8 - 5!)) = 51
#
parser.add_argument('numbers', type=int, nargs='*', default=[5, 6, 7, 8, 51],
                    help='a list of numbers, the last one is the target, and the rest '
                         'of them are source numbers.')

parser.add_argument('--factorial_upper_limit',
                    type=int,
                    default=10,
                    help="The upper limit of factorial operand. we will not try to apply "
                         "factorial operation on numbers larger than this.")

parser.add_argument('--find_all_solutions',
                    action='store_true',
                    default=False,
                    help="When specified, keep searching for more solutions "
                         "even if one solution is found.")

BINARY_OPERATORS = ['+', '-', '*', '/', 'pow']
UNARY_OPERATORS = ['u-', 'sqrt', 'factorial']


class Node:
  def __init__(self, operator, value, left, right):
    self.operator = operator
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    if self.operator is None:
      return str(self.value)
    elif self.operator in BINARY_OPERATORS:
      return '(%s %s %s)' % (self.left, self.operator, self.right)
    elif self.operator in UNARY_OPERATORS:
      return '(%s %s)' % (self.operator, self.left)

  @staticmethod
  def FromValue(value):
    return Node(None, value, None, None)

  @staticmethod
  def FromBinaryOperator(operator, left, right):
    return Node(operator, None, left, right)

  @staticmethod
  def FromUnaryOperator(operator, node):
    return Node(operator, None, node, None)


class ResultKeeper:
  def __init__(self, target_value, find_all_solutions):
    # The value to look for.
    self.target_value = target_value

    # Flag to indicate whether to stop the program if one valid expression is
    # found.
    self.find_all_solutions = find_all_solutions

    # How many expression we have seen.
    self.expression_count = 0

  def Add(self, node):
    self.expression_count += 1
    if self.expression_count % 1_000_000 == 0:
      print(f'See {self.expression_count} different expressions...')

    value = node.value
    assert not math.isnan(value), f"Invalid expression {node}"

    if self.target_value == value:
      print('Total expressions: ', self.expression_count)
      print(f'Target value {self.target_value} is found:')
      print(f'\t{node} = {self.target_value}')

      if not self.find_all_solutions:
        sys.exit(0)

  def Print(self):
    print('Total expressions: ', self.expression_count)


def ConstructExpression(node_list):
  # Apply binary operators.
  for pair in itertools.permutations(node_list, 2):
    # Remove pairs from the node list.
    left_node_list = node_list.copy()
    left_node_list.remove(pair[0])
    left_node_list.remove(pair[1])

    # Construct all the possible the new node list.
    for operator in BINARY_OPERATORS:
      new_node = Node.FromBinaryOperator(operator, pair[0], pair[1])

      # Eval the new node.
      if new_node.operator == '+':
        new_node.value = new_node.left.value + new_node.right.value

      if new_node.operator == '-':
        new_node.value = new_node.left.value - new_node.right.value

      if new_node.operator == '*':
        new_node.value = new_node.left.value * new_node.right.value

      if new_node.operator == '/':
        if new_node.right.value == 0:
          # Do not construct invalid expression.
          continue
        else:
          new_node.value = new_node.left.value / new_node.right.value

      if new_node.operator == 'pow':
        try:
          new_node.value = math.pow(new_node.left.value, new_node.right.value)
        except:
          continue

      new_node_list = left_node_list.copy()
      new_node_list.append(new_node)
      yield new_node_list

  # Apply unary operators.
  #
  # Notice that unary operators can be applied indefinitely, so to make things
  # easier, we apply some restriction to each of them. See below for details.
  for node in node_list:
    left_node_list = node_list.copy()
    left_node_list.remove(node)

    for operator in UNARY_OPERATORS:
      if operator == 'sqrt':
        if (node.value < 0 or
            node.value == 1 or
            node.value == 0 or
            math.sqrt(node.value) != int(math.sqrt(node.value))):
          continue

        new_node = Node.FromUnaryOperator('sqrt', node)
        new_node.value = math.sqrt(node.value)
        new_node_list = left_node_list.copy()
        new_node_list.append(new_node)
        yield new_node_list

      if operator == 'factorial':
        if (node.value > FLAGS.factorial_upper_limit or
            node.value < 0 or
            int(node.value) != node.value or
            node.value == 1 or   # 1! = 1
            node.value == 2):    # 2! = 2
          continue

        new_node = Node.FromUnaryOperator('factorial', node)
        new_node.value = math.factorial(node.value)
        new_node_list = left_node_list.copy()
        new_node_list.append(new_node)
        yield new_node_list

      if operator == 'u-':
        if (node.operator == 'u-' or # don't negative again.
            node.value == 0):
          continue

        new_node = Node.FromUnaryOperator('u-', node)
        new_node.value = 0 - node.value
        new_node_list = left_node_list.copy()
        new_node_list.append(new_node)
        yield new_node_list


def ProcessExpression(current_node_list, result_keeper):
  for node_list in ConstructExpression(current_node_list):
    if len(node_list) == 1:
      result_keeper.Add(node_list[0])
    else:
      ProcessExpression(node_list, result_keeper)


def main():
  global FLAGS
  FLAGS = parser.parse_args()
  if len(FLAGS.numbers) < 2:
    print("At least two numbers should be specified.")
    parser.print_usage()
    sys.exit(0)

  START_NODE_LIST = []
  for number in FLAGS.numbers[:-1]:
    START_NODE_LIST.append(Node.FromValue(int(number)))
  TARGET = int(FLAGS.numbers[-1])

  result_keeper = ResultKeeper(TARGET, FLAGS.find_all_solutions)
  ProcessExpression(START_NODE_LIST, result_keeper)
  result_keeper.Print()


if __name__ == '__main__':
  main()
