s = input("Enter string: ")

words = s.split()
result = ""

for w in words:
    chars = sorted(w)
    
    word = ""
    for c in chars:
        word += c
    
    result += word + " "

print("Result:", result)
