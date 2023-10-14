# Write a Python program to get the execution time of a Python method.

import time

def sum_of_n(n):
    start_time = time.time_ns()
    sum = 0
    for i in range(1, n):
        sum += i
    end_time = time.time_ns()
    return sum, end_time-start_time

print("Sum: %d\n Time Taken: %d" %sum_of_n(500000))