# Write a Python program to prove that two string variables of the same value point to the same memory location.

str1 = "Python"
str2 = "Python"

print("Memory location of str1:", id(str1))
print("Memory location of str2:", id(str2))

list1 = [10, 20, 30, 40]
list2 = [10, 20, 30, 40]
list3 = list1
print("Memory location of list1:", id(list1))
print("Memory location of list3:", id(list3))
print("Memory location of list2:", id(list2))