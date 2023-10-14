# Program to print first and last color from given color list.

color_list = input("Enter colors: ").split()
print(color_list)

first_color = color_list[0]
last_color = color_list[-1]

#print("First color: " + first_color + ", Last color: " + last_color)

print("First color: %s, Last color: %s" %(first_color, last_color))