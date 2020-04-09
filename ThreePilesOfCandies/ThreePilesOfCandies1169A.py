q = int(input())
for i in range(q):
    s = sum([int(x) for x in input().split(" ")])
    print(s//2)
