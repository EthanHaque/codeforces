n = int(input())
i, j = 0, 0
for l in range(n):
    m, c = map(int, input().split(" "))
    if(m > c):
        i += 1
    elif(m < c):
        j += 1
    
if(i>j):
    print("Mishka")
elif(i<j):
    print("Chris")
else:
    print("Friendship is magic!^^")
