# Program to concatenate all elements in a list into a string

given_list = input("Enter name list: ").split()

print(type(given_list))

concatenated_list = "".join(given_list)

print("concatenated string: ", concatenated_list)
print(type(concatenated_list))