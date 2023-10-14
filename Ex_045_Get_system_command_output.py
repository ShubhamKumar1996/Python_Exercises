# Write a Python program to get system command output.

import subprocess

# files and directory listing
result = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(result)