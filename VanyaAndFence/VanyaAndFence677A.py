n, h = map(int, input().split(" "))
a = [int(x) for x in input().split(" ")]

count = 0
for i in a:
    if(i > h):
        count += 2
    else:
        count += 1
print(count)