def inside_circle(x, y, a, b, R):
    return (x - a) ** 2 + (y - b) ** 2 < R ** 2

a = float(input("Enter center x (a): "))
b = float(input("Enter center y (b): "))
R = float(input("Enter radius R: "))

points = []

for i in range(3):
    x = float(input(""))
    y = float(input(""))
    points.append((x, y))

count = 0
for x, y in points:
    if inside_circle(x, y, a, b, R):
        count += 1

print("Points inside the circle:", count)
