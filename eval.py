#!/usr/bin/python3

import itertools
import math
import sys

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
      return '(%s) %s (%s)' % (self.left, self.operator, self.right)
    elif self.operator in UNARY_OPERATORS:
      return '%s (%s)' % (self.operator, self.left)

  @staticmethod
  def FromValue(value):
    return Node(None, value, None, None)

  @staticmethod
  def FromOperator(operator, left, right):
    return Node(operator, None, left, right)


def Eval(node):
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

    # FIXME: Facotrial has upper limit 10.
    if left_value > 10 or left_value < 0 or int(left_value) != left_value:
      return math.nan

    return math.factorial(left_value)


class ResultKeeper:
  def __init__(self, target_value=51):
    self.target_value = target_value

    self.expression_count = 0
    self.invalid_expression_count = 0
    self.valid_expression_count = 0

  def Add(self, node):
    self.expression_count += 1
    if self.expression_count % 1_000_000 == 0:
      print(f'See {self.expression_count} different expressions...')

    value = Eval(node)
    if math.isnan(value):
      self.invalid_expression_count += 1
      return

    self.valid_expression_count += 1

    if self.target_value == value:
      print('Total expressions: ', self.expression_count)
      print('Total invalid expressions: ', self.invalid_expression_count)
      print('Total valid expression: ', self.valid_expression_count)
      print(f'Target value {self.target_value} is found:')
      print(f'\t{node} = {self.target_value}')

      # Early quit since the amouont of the expression is too large.
      sys.exit(0)

  def Print(self):
    print('Total expressions: ', self.expression_count)
    print('Total invalid expressions: ', self.invalid_expression_count)
    print('Total valid expression: ', self.valid_expression_count)


def ConstructExpression(node_list):
  # Apply binary operators.
  for pair in itertools.permutations(node_list, 2):
    # Remove pairs from the node list.
    left_node_list = node_list.copy()
    left_node_list.remove(pair[0])
    left_node_list.remove(pair[1])

    # Construct all the possible the new node list.
    for operator in BINARY_OPERATORS:
      new_node = Node.FromOperator(operator, pair[0], pair[1])
      new_node_list = left_node_list.copy()
      new_node_list.append(new_node)
      yield new_node_list

  # Apply unary operators.
  #
  # Notice that unary operators can be applied indefinitely, so to make things
  # easier, we apply at most 1 times.
  for node in node_list:
    # FIXME: There is better way to handle this. Namely we compute the value and
    # then check if it is appropriate to apply the operator to the value. Such
    # factorial of 100000 (not good), or sqrt of -30 (not good).
    if node.operator in UNARY_OPERATORS:
      continue

    left_node_list = node_list.copy()
    left_node_list.remove(node)

    # FIXME: the amount of expressions increase expoentially with the amount of
    # unary operators we want to try. For this specific problem, sqrt seems to
    # be unnecessary.
    #new_node = Node.FromOperator('sqrt', node, None)
    #new_node_list = left_node_list.copy()
    #new_node_list.append(new_node)
    #yield new_node_list

    new_node = Node.FromOperator('factorial', node, None)
    new_node_list = left_node_list.copy()
    new_node_list.append(new_node)
    yield new_node_list

    # FIXME: the amount of expressions increase expoentially with the amount of
    # unary operators we want to try. For this specific problem, u- seems to
    # be unnecessary.
    #new_node = Node.FromOperator('u-', node, None)
    #new_node_list = left_node_list.copy()
    #new_node_list.append(new_node)
    #yield new_node_list


def ProcessExpression(current_node_list, result_keeper):
  for node_list in ConstructExpression(current_node_list):
    if len(node_list) == 1:
      result_keeper.Add(node_list[0])
    else:
      ProcessExpression(node_list, result_keeper)

#
# 6 - (7! / (8 - 5!)) = 51
#
if len(sys.argv) == 1:
  START_NODE_LIST = [
     Node.FromValue(5),
     Node.FromValue(6),
     Node.FromValue(7),
     Node.FromValue(8),
     ]
  TARGET = 51
elif len(sys.argv) >=3:
  START_NODE_LIST = []
  for arg in sys.argv[1:-1]:
    START_NODE_LIST.append(Node.FromValue(int(arg)))
  TARGET = int(sys.argv[-1])
else:
  print(f'Invalid argument. Usage:\n'
        f'\t{sys.argv[0]}\n'
        f'\t{sys.argv[0]} <source>[...] <target>')
  sys.exit(0)

result_keeper = ResultKeeper(TARGET)
ProcessExpression(START_NODE_LIST, result_keeper)
result_keeper.Print()
