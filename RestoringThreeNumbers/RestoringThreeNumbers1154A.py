n = sorted(list(map(int, input().split())))

c = n[3] - n[0]
a = n[1] - c
b = n[2] - c
print(a, b, c)