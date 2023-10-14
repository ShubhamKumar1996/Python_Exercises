# Program to calculate the area of circle based on radius.

from math import pi,pow

# Collect radius from user.
radius = float(input("Radius: "))

# Compute area
# area = pi * radius * radius
# area = pi * pow(radius, 2)
area = pi * radius**2

# Print area
print(area)