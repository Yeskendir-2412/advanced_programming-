a = int(input())
b = int(input())
c = int(input())
max = 0
min = 0
if a > b and a >c:
    max = a 
    if b > c:
        min = c 
    else:
        min =b
elif b > a and b >c:
    max = b
    if a > c:
        min = c
    else:
        min = a
elif c > a and c >b:
    max = c
    if a > b:
        min = b
    else:
        min = a

print(max - min)