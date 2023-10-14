# Program to check whether Python shell is executing in 32bit or 64bit mode on OS

import platform

print(platform.architecture()[0])