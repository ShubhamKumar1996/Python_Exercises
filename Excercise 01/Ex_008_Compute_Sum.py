# Program to compute (n + nn + nnn) with given n.

n = input("n: ")

# Computing n, nn, nnn
n1 = int("%s" % n)
n2 = int("%s%s" %(n, n))
n3 = int("%s%s%s" %(n, n, n))

calculated_sum: int = n1 + n2 + n3

print('Sum: {:d}'.format(calculated_sum))