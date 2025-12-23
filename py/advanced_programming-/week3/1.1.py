def ca(r):
    return 3.14 * r * r

def ra(a, b):
    return a * b

def ta(a, h):
    return 0.5 * a * h

def ba(r):
    return 3.14 * r * r * 4

a = input("1 = circle , 2 = rectangle , 3 = triangle , 4 = Square , 5 = Ball")
if a == "1":
    i1 = float(input())
    print(ca(i1))
elif a == "2":
  i2 = float(input())
  i3 = float(input())
  print(ra(i2,i3))
elif a == "3":
   i4 = float(input())
   i5 = float(input())
   print(ta(i4,i5))
elif a == "4":
    a = int(a)
    print(a * a)
elif a =="5":
    i6 = float(input())
    print(ba(i6))
else:
    print("Error")
