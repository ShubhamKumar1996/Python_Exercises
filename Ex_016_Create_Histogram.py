# Program to create histogram from given list.

import matplotlib.pyplot as plt

arr = list(map(int, input("Enter list: ").split()))

# check how to create histogram.
plt.hist(arr)
plt.show()