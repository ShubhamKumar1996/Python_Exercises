# Write a Python program to get the current value of the recursion limit.

import sys

print("Value of recursion limit: %d" % sys.getrecursionlimit())

sys.setrecursionlimit(10000)

print("Value of recursion limit: %d" % sys.getrecursionlimit())