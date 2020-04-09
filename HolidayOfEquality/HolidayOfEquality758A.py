n = int(input())
t = [int(x) for x in input().split(" ")]

print(round((max(t)-sum(t)/n) * n))