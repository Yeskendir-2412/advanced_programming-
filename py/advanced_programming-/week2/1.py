arrow1 = ">>-->" 
arrow2 = "<--<<" 
legolas = str(input("Enter the string: ")) 
arrow = 0
for i in range(len(legolas)-4): 
    if legolas[i:i+5] == arrow1 or legolas[i:i+5] == arrow2: 
        arrow += 1 
print("arrows.count:", arrow)