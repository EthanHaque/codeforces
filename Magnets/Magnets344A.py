n, count = int(input()), 0
previous = input()

for i in range(n-1):
    current = input()
    if(previous != current):
        count += 1
    previous = current
print(count + 1)
    