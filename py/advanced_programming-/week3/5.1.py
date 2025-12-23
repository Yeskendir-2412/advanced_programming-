def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a

A = float(input())
B = float(input())
C = float(input())
D = float(input())

n = A*D - C*B
d = B*D

g = gcd(n, d)

print("Result:", n//g, "/", d//g)
