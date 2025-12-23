def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Enter array length: "))
A = []
for i in range(m):
    x = int(input())
    A.append(x)
print("Original", A)

swap(A)

print("swap:", A)
