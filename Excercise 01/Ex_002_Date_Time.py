# Program to print current date & time.
# Printing date time can be used while printing logs

import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
print(datetime.date.today())