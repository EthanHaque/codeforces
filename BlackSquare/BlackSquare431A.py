cal = [int(x) for x in input().split(" ")]
s = input()
count = 0
for char in s:
    count += cal[int(char)-1]
print(count)