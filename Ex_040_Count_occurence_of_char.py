# Write a Python program to count the number of occurrences of a specific character in a string.

# Approach 1
s = "Python program to count the number of occurrences of a specific character in a string"
count = s.count('P')
print("Count1: ", count)

# Approach 2
from collections import Counter

counter = Counter(s)
print("Count2: ", counter['o'])

# Approach 3
count = sum(map(lambda word: 1 if 't' in word else 0, s))
print("Count3: ", count)

# Approach 4
import re

count = len(re.findall('h', s))
print("Count4: ", count)