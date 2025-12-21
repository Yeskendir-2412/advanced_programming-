# a = abcabc
# b = abc

# abc
# bca
# cab

# abc  +1
# bca  +1
# cab  +1
# abc  +1

w1 = input()
w2 = input()
l = len(w2)
rot = set()
l1 = w2 + w2
c = 0
for i in range(l):
    rot.add(l1[i:i+l])

for i in range(len(w1)-l+1):
    if w1[i:i+l] in rot:
        c+=1
print(c)


