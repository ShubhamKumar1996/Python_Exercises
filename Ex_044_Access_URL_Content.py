# Write a Python program to access and print a URL's content to the console.

from http.client import HTTPConnection

connection = HTTPConnection("www.google.com")
connection.request("GET", "/")
result = connection.getresponse()
# retrieves the entire contents.
contents = result.read()
print(contents)