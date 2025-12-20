task3 = input("You must put 1st,3rd and 5th only number(0-9) or number you hide 2nd(+,-) and 4th must be operation (=) ")
n1 = task3[0]
o1 = task3[1]
n2 = task3[2]
n3 = task3[4]

if n1 == "x":
    n3 = int(n3)
    n2 = int(n2)
    if o1 == "-":
        print(n3+n2)
    else:
        print(n3-n2)
elif n2 == "x":
    n3 = int(n3)
    n1 = int(n1)
    if o1 == "-":
        print(n1-n3)
    else:
        print(n3-n1)
elif n3 == "x":
    n2 = int(n2)
    n1 = int(n1)
    if n3 =="-":
        print(n1-n2)
    else:
        print(n1+n2)
    