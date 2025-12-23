def right_triangle_area(a, b):
    return 0.5 * a * b

def rectangle_area(a, b):
    return a * b

X = float(input(" "))
Y = float(input(""))
Z = float(input(""))
T = float(input(""))

a = right_triangle_area(X, Y) + rectangle_area(Z, T)
print(a)
