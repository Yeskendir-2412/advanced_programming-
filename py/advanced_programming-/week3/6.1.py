def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("Enter A: "))
B = int(input("Enter B: "))

gcd1 = gcd(A, B)
lcm = A * B // gcd1

print("GCD:", gcd1)
print("LCM:", lcm)
