# Task

# You are given a two lists A and B. Your task is to compute their cartesian product AXB.

# Sample Input
#  1 2
#  3 4

# Sample Output
 # (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product
A = map(int,input().split())
# a = [int(i) for i in A]
B = input().split()
b = [int(x) for x in B]
print(*product(A,b))
