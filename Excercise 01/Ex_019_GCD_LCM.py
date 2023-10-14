# Program to compute Greatest common divisor (GCD) & Least common multiple (LCM) of two positive integers

from math import gcd, lcm


def compute_gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    return compute_gcd(num2, num1 % num2)


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# computed_gcd = gcd(num1, num2)
# computed_lcm = lcm(num1, num2)

computed_gcd: int = compute_gcd(num1, num2)
computed_lcm = (num1 * num2) / computed_gcd

print("GCD: %d, LCM: %d" % (computed_gcd, computed_lcm))
