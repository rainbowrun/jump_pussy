#!/usr/bin/python3

import math

def Choose(n, k):
  assert n>0
  assert k>0
  assert n>=k

  return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

print(Choose(5,3))

def X(n, k):
  if k == 1:
    return 1

  assert n>0
  assert k>0
  assert n>=k

  total = math.pow(k, n)

  for i in range(1, k):
    print(f'Consider Choose({k}, {i}) ...')
    total -= Choose(k, i) * X(n, k-i)

  return total

print(X(3, 2))
print(X(4, 3))
