a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print(a, "+", b, "=", a + b)
elif op == "-":
    print(a, "-", b, "=", a - b)
elif op == "*":
    print(a, "*", b, "=", a * b)
elif op == "/":
    if b == 0:
        print("Error")
    else:
        print(a, "/", b, "=", a / b)
else:
    print("Error")