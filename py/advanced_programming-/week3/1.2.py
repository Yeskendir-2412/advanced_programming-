arrays = []

for i in range(3):
    line = input()
    
    arr = [float(x) for x in line.split()]
    
    if len(arr) > 15:
        print("Error")
        arr = arr[:15]
        
    arrays.append(arr)

print("-" * 30)

for a in arrays:
    s = sum(a)
    avg = s / len(a)
    print("Array:", a)
    print("Sum:", s)
    print("Average:", avg)
    