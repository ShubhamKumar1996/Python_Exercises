# Program to List all files in a directory in Python

from os import listdir
from os.path import isfile, join

files_list = []
DIR_STR = "C:\\Users\\shubham\\PycharmProjects\\pythonProject\\Excercises"
for file in listdir(DIR_STR):
    file_name = join(DIR_STR, file)
    if isfile(file_name):
        files_list.append(file)


print(files_list)