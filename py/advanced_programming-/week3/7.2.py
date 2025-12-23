a = int(input())
if a < 0:
    print("Error")
else:
    oc = ""
    if a == 0:
        oc="0"
    else:
        t = a
        while t >0:
            o = t %8
            oc =  str(o) + oc
            t = t//8
    while len(oc) < 10:
        oc = "0" + oc
print(oc)