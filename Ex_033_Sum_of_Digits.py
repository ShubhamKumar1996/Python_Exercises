# Write a Python program to calculate sum of digits of a number.

def digit_sum(num: int) -> int:
    sum = 0
    while num > 0:
        sum += num % 10
        num = num//10
    return sum


print(digit_sum(256))