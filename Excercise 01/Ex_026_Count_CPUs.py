# Program to Check number of CPUs

import multiprocessing
import os

print(multiprocessing.cpu_count())
print(os.cpu_count())