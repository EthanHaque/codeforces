count = 0
n = int(input())

while(n != 0):
    if(n >= 100000):
        n -= 100000
        count += 999
    elif(n >= 1000):
        n -= 1000
        count += 9
    elif(n >= 100):
        n -= 100
    elif(n >= 20):
        n -= 20
    elif(n >= 10):
        n -= 10
    elif(n >= 5):
        n -= 5
    else:
        n -= 1
    count += 1

print(count)
