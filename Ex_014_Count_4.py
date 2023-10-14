# Program to count 4 in given list.

def count4(given_list):
    count = 0
    for num in given_list:
        if num == 4:
            count += 1
    return count


# given_str_list = input("Enter List: ").split()
# given_list = [int(num) for num in given_str_list]

# given_list = input("Enter List: ").split()
# for i in range(len(given_list)):
#     given_list[i] = int(given_list[i])

given_list = list(map(int, input("Enter List: ").split()))

print(count4(given_list))