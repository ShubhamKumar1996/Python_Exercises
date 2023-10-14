# Write a Python program to get the details of the math module.

import math

# Collects the list of attribute of math modules.
math_attribute_list = dir(math)
print(math_attribute_list)

# Brief documentation of math module
print("\n", math.__doc__)

# Detailed documentation of math module
help(math)