# Program to get the path and name of the file that is currently executing

import os

print("Current File Relative Path:", os.path.relpath(__file__))
print("Current File Absolute Path:", os.path.abspath(__file__))