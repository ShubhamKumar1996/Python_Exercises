# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys

print(sys.argv)

print("Script Name: ", sys.argv[0])

for i in range(1, len(sys.argv)):
    print("Arg %d: %s" % (i, sys.argv[i]))