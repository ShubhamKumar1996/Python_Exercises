# Program to get list and tuple from comma separated number string

num_str = input("number string: ")

num_list = num_str.split(',')
num_tuple = tuple(num_list)

print(num_list)
print(num_tuple)