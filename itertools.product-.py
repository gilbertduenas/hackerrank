# https://www.hackerrank.com/challenges/itertools-product/problem
# learn to splat

from itertools import product

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(*product(x, y))
