n = int(input())
k = list(input().split(" "))

flag = True

for i in range(n):
    if k[i] == "1":
        flag = False
        
if(flag):
    print("EASY")
else:
    print("HARD")