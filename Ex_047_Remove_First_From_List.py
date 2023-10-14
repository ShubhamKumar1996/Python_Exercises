# Write a Python program to remove the first item from a specified list.

# Approach 1
num_list = [10, 12, 14, 17, 19, 23]
print("Original List: ", num_list)
del num_list[0]
print("List after deletion: ", num_list)

# Approach 2
num_list2 = [10, 12, 14, 17, 19, 23]
print("Original List: ", num_list2)
new_num_list2 = num_list2[1:]
print("List after deletion: ", new_num_list2)

# Approach 3
num_list3 = [10, 20, 30, 40, 50, 30]
print("Original List: ", num_list3)
num_list3.remove(30)    # Removes only first instance
print("List after deletion: ", num_list3)