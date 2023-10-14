# Program to print out a set containing all the colors from a list which are not present in other list

list_str1 = input("Enter list_str1: ").split()
list_str2 = input("Enter list_str2: ").split()

# for color in list_str1:
#     if not(color in list_str2):
#         print(color)

set1 = set(list_str1)
set2 = set(list_str2)
# print(set1.difference(set2))
# print(set2.difference(set1))

print(set1 - set2)
print(set2 - set1)