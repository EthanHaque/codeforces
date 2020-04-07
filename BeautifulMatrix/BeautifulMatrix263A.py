matrix = [input().split() for x in range(5)]
i, j = 0, 0

for y in matrix:
    for x in y:
        if(x == "1"):
            i, j = matrix.index(y), y.index(x)
print(abs(2-i) + abs(2-j))
            
