#!/usr/bin/python3

import itertools
import math
import sys

class Node:
  def __init__(self, operator, value, left, right):
    self.operator = operator
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    if self.value is not None:
      return str(self.value)
    else:
      return '(%s) %s (%s)' % (self.left, self.operator, self.right)

  @staticmethod
  def FromValue(value):
    return Node(None, value, None, None)

  @staticmethod
  def FromOperator(operator, left, right):
    return Node(operator, None, left, right)


# Possible operators.
OPERATORS = [
      '+',           # Addition
      '-',           # Subtract
      '*',           # Multiplication
      '/',           # Division
      'pow',         # Power
      'sqrt',        # Square root
      'factorial',   # Factorial
      'u-',          # Unary Subtract
      ]


def Eval(node):
  assert node, "Invalid node"
  assert node.operator in OPERATORS or node.operator is None

  if node.operator is None:
    assert node.value is not None, "Invalid node value"
    return node.value

  if node.operator == '+':
    return Eval(node.left) + Eval(node.right)

  if node.operator == '-':
    return Eval(node.left) - Eval(node.right)

  if node.operator == '*':
    return Eval(node.left) * Eval(node.right)

  if node.operator == '/':
    right_value = Eval(node.right)
    if right_value == 0:
      return math.nan
    else:
      return Eval(node.left) / right_value

  if node.operator == 'pow':
    try:
      return math.pow(Eval(node.left), Eval(node.right))
    except:
      return math.nan

  if node.operator == 'u-':
    return 0 - Eval(node.left)

  if node.operator == 'sqrt':
    left_value = Eval(node.left)
    if left_value < 0:
      return math.nan
    else:
      return math.sqrt(left_value)

  if node.operator == 'factorial':
    left_value = Eval(node.left)

    if math.isnan(left_value):
      return math.nan

    if left_value > 10 or left_value < 0 or int(left_value) != left_value:
      return math.nan

    return math.factorial(left_value)


class ResultKeeper:
  def __init__(self, target_value=51):
    # Key is expression value, value is one of the expression to get
    # this value.
    self.results = {}

    self.expression_count = 0
    self.invalid_expression_count = 0

    self.target_value = target_value

  def Add(self, node):
    self.expression_count += 1
    if self.expression_count % 1_000_000 == 0:
      print(f'See {self.expression_count} different expressions...')

    value = Eval(node)
    if math.isnan(value):
      self.invalid_expression_count += 1
      return

    if value not in self.results:
      self.results[value] = node

    # FIXME: Early quit since the overall number is too large.
    if self.target_value in self.results:
      print(f'Target value {self.target_value} is found:')
      print('%s = %s' % (self.results[self.target_value], self.target_value))
      sys.exit(0)

  def Print(self):
    for value in self.results:
      print('%s = %s' % (self.results[value], value))

    print('Total expressions: ', self.expression_count)
    print('Total invalid expressions: ', self.invalid_expression_count)
    print('Total values: ', len(self.results))
    if self.target_value in self.results:
      print(f'Target value {self.target_value} is found:')
      print('%s = %s' % (self.results[self.target_value], self.target_value))
    else:
      print(f'Target value {self.target_value} is NOT found.')


if len(sys.argv) == 1:
  result_keeper = ResultKeeper(51)
elif len(sys.argv) == 2:
  result_keeper = ResultKeeper(int(sys.argv[1]))
else:
  print('Usage %s [target_value]' % sys.argv[0])
  sys.exit(0)


def ConstructExpression(node_list):
  # Apply binary operators.
  for pair in itertools.permutations(node_list, 2):
    # Remove pairs from the node list.
    left_node_list = node_list.copy()
    left_node_list.remove(pair[0])
    left_node_list.remove(pair[1])

    # Construct all the possible the new node list. 
    for operator in ['+', '-', '*', '/', 'pow']:
      new_node = Node.FromOperator(operator, pair[0], pair[1])
      new_node_list = left_node_list.copy()
      new_node_list.append(new_node)
      yield new_node_list

  # Apply unary operators. For these operators, we construct some aux node
  # to help evaluate.
  #
  # Notice that unary operators can be applied indefinitely, so to make things
  # easier, we limit to apply at most 1 times.
  UNARY_OPERATORS = ['u-', 'sqrt', 'factorial']
  for node in node_list:
    # FIXME: There is better way to handle this.
    if node.operator in UNARY_OPERATORS:
      continue

    left_node_list = node_list.copy()
    left_node_list.remove(node)

    # FIXME
    # new_node = Node.FromOperator('sqrt', node, None)
    # new_node_list = left_node_list.copy()
    # new_node_list.append(new_node)
    # yield new_node_list

    new_node = Node.FromOperator('factorial', node, None)
    new_node_list = left_node_list.copy()
    new_node_list.append(new_node)
    yield new_node_list

    new_node = Node.FromOperator('u-', node, None)
    new_node_list = left_node_list.copy()
    new_node_list.append(new_node)
    yield new_node_list


def ProcessExpression(current_node_list):
  for node_list in ConstructExpression(current_node_list):
    if len(node_list) == 1:
      result_keeper.Add(node_list[0])
    else:
      ProcessExpression(node_list)

START_NODE_LIST = [
   Node.FromValue(5),
   Node.FromValue(6),
   Node.FromValue(7),
   Node.FromValue(8),
   ]

ProcessExpression(START_NODE_LIST)
result_keeper.Print()

#import pdb; pdb.set_trace()  FIXME
