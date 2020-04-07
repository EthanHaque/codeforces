n, t, sf, fs = int(input()), input(), 0, 0
for i in range(n-1):
    if(t[i] == "S" and t[i+1] == "F"):
        sf += 1
    elif(t[i] == "F" and t[i+1] == "S"):
        fs += 1 

print("YES") if sf > fs else print("NO")