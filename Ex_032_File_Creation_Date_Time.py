# Write a Python program that retrieves the date and time of file creation and modification.

import os.path, time

FILE_STR = "Ex_000_Test.py"

creation_date_time = time.ctime(os.path.getctime(FILE_STR))
modification_date_time = time.ctime(os.path.getmtime(FILE_STR))

print("File Creation date time: %s" % creation_date_time)
print("File Modification date time: %s" % modification_date_time)
