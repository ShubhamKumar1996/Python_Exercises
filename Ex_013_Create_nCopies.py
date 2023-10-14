# Program to create n copies of given string.

input_str = input("String: ")
n = int(input("n: "))

result = ""

for i in range(n):
    result = result + input_str

print(result)