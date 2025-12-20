al = set("ABCEHKMOPTXY")

def i(s):
    if len(s) != 6:
        return False
    
    parts = [
        s[0] in al,
        s[1:4].isdigit(),
        s[4] in al,
        s[5] in al
    ]
    return all(parts)

n = int(input())
for _ in range(n):
    s = input()
    if i(s):
        print("Yes")
    else:
        print("No")