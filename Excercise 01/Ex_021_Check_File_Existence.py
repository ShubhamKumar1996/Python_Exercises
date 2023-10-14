# Program to check if file exits

import os

print(os.path.isfile("Ex_020_Is_Integer_Object.py"))    # Only check for file existence
print(os.path.isfile("Ex_022_test.py"))

print(os.path.exists("Ex_020_Is_Integer_Object.py"))    # Check for file & directory existence.
print(os.path.exists("Ex_022_test.py"))

# 3rd Approach
try:
    file_obj = open("Ex_000_Test.py")
    file_obj.close()
    print("File Found")
except FileNotFoundError:
    print("File not found")

try:
    file_obj = open("Ex_000.py")
    file_obj.close()
    print("File Found")
except FileNotFoundError:
    print("File not found")