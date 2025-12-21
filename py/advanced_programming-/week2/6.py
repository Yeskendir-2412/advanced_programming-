def all_eq(strings):
    max = 0
    for i in strings:
        if len(i) > max:
            max = len(i)
    
    result = []
    for a in strings:
        pos = max - len(a)
        result.append(a + pos * b)
    
    return result
a = int(input("Кол строк:"))
b = input("Что хочешь добавить место пустоты?:")
add = []
for i in range(a):
    s = input()
    add.append(s)
print(all_eq(add))

