products = input().split()
counts = {}

for i in products:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print("Purchase frequency:")
for i in counts:
    print(i + ":", counts[i])

max_product = None
max_count = 0

for i in counts:
    if counts[i] > max_count:
        max_count = counts[i]
        max_product = i

print("Most popular item:", max_product)

print("Purchased once:")
for i in counts:
    if counts[i] == 1:
        print(i)

print("Sorted by frequency:")
max_count = 0
for i in counts:
    if counts[i] > max_count:
        max_count = counts[i]

for c in range(max_count, 0, -1):
    for i in counts:
        if counts[i] == c:
            print(i, counts[i])
