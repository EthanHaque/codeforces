n = int(input())
arr = input().split(" ")
p = [0] * n
count = 0
out = ""
for i in arr:
    p[int(i)-1] = count + 1
    count += 1

for x in p:
    out += str(x) + " "

print(out)
