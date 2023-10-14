# Program to access environment variables.

import os

for key, value in os.environ.items():
    print("%s: %s" %(key, value))