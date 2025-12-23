import math
print("First angles:")
def hyp(a , b):
    return math.sqrt(a*a + b*b)
a1=float(input())
a2=float(input())
print("Second angles:")
a3=float(input())
a4=float(input())
if a1 <= 0 and a2 <= 0 and a3 <= 0 and a4 <= 0:
    print("Error")
h1 = hyp(a1,a2)
h2= hyp(a3,a4)

if h1>h2:
    print("Hyp1 greater then Hyp2")
else:
    print("Hyp2 greater then Hyp1")
