ticket = int(input("6-digit number pls:"))
a = ticket // 100000       
b = ticket // 10000 % 10   
c = ticket // 1000 % 10    
d = ticket // 100 % 10     
e = ticket // 10 % 10      
f = ticket % 10   
if a + b + c == d + e + f:
    print("YES")
else:
    print("NO")