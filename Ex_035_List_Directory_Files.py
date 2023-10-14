# Write a Python program to get a directory listing, sorted by creation date.

import os
import time

file_list = []
for file in os.listdir("."):
    creation_time = time.ctime(os.path.getctime(file))
    file_list.append((creation_time, file))

sorted_file_list = sorted(file_list, key=lambda x: x[0])

print(sorted_file_list)