# Program to append "ls" to given string is not already found in the beginning.

def is_prefix_found(given_str):
    if len(given_str) > 1 and given_str[:2] == "ls":
        return True
    return False


input_str = input("Enter String: ")

if not is_prefix_found(input_str):
    input_str = "ls" + input_str

print(input_str)
