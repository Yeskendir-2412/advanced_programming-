import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
diagonal = float(input("Enter diagonal: "))

p1 = (a + b + diagonal) / 2
p2 = (c + d + diagonal) / 2

area1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - diagonal))
area2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - diagonal))

total_area = area1 + area2

print("Area of quadrilateral:", total_area)
