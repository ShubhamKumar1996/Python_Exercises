# Write a Python program to get the size of an object in bytes.
import sys

str1 = "abc"
str2 = "ab"
num1 = 1
num2 = 12

print("Size of str1 in byte: %d" % sys.getsizeof(str1))
print("Size of str2 in byte: %d" % sys.getsizeof(str2))
print("Size of num1 in byte: %d" % sys.getsizeof(num1))
print("Size of num2 in byte: %d" % sys.getsizeof(num2))