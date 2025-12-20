f1, f2 = map(int, input().split())
f = input()

words = []

for i in range(f1 - f2 + 1):
    part = f[i:i+f2]
    if part not in words:
        words.append(part)

print(len(words))
