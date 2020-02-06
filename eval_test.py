#!/usr/bin/python3

import math

from eval import Node, Eval, ConstructExpression

node1 = Node.FromValue(1)
node2 = Node.FromValue(2)
node3 = Node.FromOperator('+', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('-', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('*', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('/', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('pow', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('sqrt', node1, node2)
print(str(node3), '=', Eval(node3))

node1 = Node.FromValue(0)
node2 = Node.FromValue(0)
node3 = Node.FromOperator('+', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('-', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('*', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('/', node1, node2)
print(str(node3), '=', Eval(node3))

node3 = Node.FromOperator('pow', node1, node2)
print(str(node3), '=', Eval(node3))

node1 = Node.FromValue(16)
node2 = Node.FromValue(2)
node3 = Node.FromOperator('sqrt', node1, node2)
print(str(node3), '=', Eval(node3))

node1 = Node.FromValue(-16)
node2 = Node.FromValue(2)
node3 = Node.FromOperator('sqrt', node1, node2)
print(str(node3), '=', Eval(node3))

node1 = Node.FromValue(16)
node2 = Node.FromValue(2)
node3 = Node.FromOperator('sqrt', node1, node2)
node4 = Node.FromValue(5)
node5 = Node.FromValue(3)
node6 = Node.FromOperator('*', node4, node5)
node7 = Node.FromOperator('+', node3, node6)
print(str(node7), '=', Eval(node7))

start_node_list = [
   Node.FromValue(5),
   Node.FromValue(6),
   Node.FromValue(7),
   Node.FromValue(8),
   ]

for node_list in ConstructExpression(start_node_list):
  print('node_list:')
  for node in node_list:
    print(f'\t{node}')

