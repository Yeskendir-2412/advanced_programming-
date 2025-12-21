print("words must be the same length")
word1 = input()
word2 = input()
if len(word1) != len(word2):
    print("no")
else:
    ok = True

    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            ok = False
            break

    if ok:
        print("yes")
    else:
        print("no")