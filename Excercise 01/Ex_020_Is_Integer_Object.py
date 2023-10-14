# Program to add two objects if both objects are an integer type.

def add_num(num1, num2):
    if not(isinstance(num1, int)) or not(isinstance(num2, int)):
        return "Input must be integer"
    return num1 + num2

print(add_num(10, 15))
print(add_num("10", "15"))
print(add_num(10, "15"))
print(add_num("10", 15))