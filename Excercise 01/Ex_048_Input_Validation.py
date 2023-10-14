# Write a Python program that inputs a number and generates an error message if it is not a number.

while True:
    try:
        num = int(input("Enter num:"))
        print(num)
        break
    except ValueError:
        print("This is not a number. Try again")

