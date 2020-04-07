n = int(input())
total = 0
for i in range(n):
    shape = input()
    if(shape[0]) == "I":
        total += 20
    elif(shape[0]) == "D":
        total += 12
    elif(shape[0]) == "O":
        total += 8
    elif(shape[0]) == "C":
        total += 6
    else:
        total += 4

print(total)
