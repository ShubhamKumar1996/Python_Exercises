# Program to print extension from the file name received from user.

filename = input("Enter filename with extension: ")

# extension = filename.split(sep='.')[-1]
extension = filename.rsplit(sep='.', maxsplit=1)[1]

print(extension)