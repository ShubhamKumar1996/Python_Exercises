# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

num_list = [45, 55, 60, 37, 100, 105, 220]

# Use Anonymous function to filter.
result = list(filter(lambda num: (num % 15 == 0), num_list))
print("Num divisible by 15: ", result)