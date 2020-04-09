a, b =  map(int, input().split(" "))

print(str(min(a, b)) + " " + str(max((a-b)//2, (b-a)//2)))