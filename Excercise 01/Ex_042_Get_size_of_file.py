# Write a Python program to get the size of a file.

# Approach 1
import os

file_size = os.path.getsize("Ex_000_Test.py")
print("The size of file1:", file_size)

# Approach 2
file_size = os.stat("Ex_000_Test.py")
print("The size of file2:", file_size.st_size)

