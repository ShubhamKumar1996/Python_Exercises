# Write a Python program to sort files by date

import glob
import os.path

FILE_STR = "C:\\Users\\shubham\\PycharmProjects\\pythonProject\\Excercises\\*"
files = glob.glob(FILE_STR)
files.sort(key=os.path.getmtime)
print("\n".join(files))