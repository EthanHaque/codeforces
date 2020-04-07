a = int(input())
outstring = ""

for i in range(a-1):
    if((i+1) % 2 == 0):
        outstring += "I love that "
    else:
        outstring += "I hate that "
if(a % 2 == 0):
    outstring += "I love it"
else:
    outstring += "I hate it"
print(outstring)