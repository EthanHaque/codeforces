n = int(input())
out = ""
flag = False
for i in range(n):
    config = input()
    if("OO" in config and not flag):
        out += config.replace("OO", "++", 1) + "\n"
        flag = True
    else:
        out += config + "\n"

if(flag):
    print("YES")
    print(out)
else:
    print("NO")
