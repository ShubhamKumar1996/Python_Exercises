# Write a Python program to print the current call stack

import traceback

print()


def function1():
    return function2()


def function2():
    traceback.print_stack()


function1()