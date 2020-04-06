n = int(input())
result = 0
i = 1
while( i <= n/2):
    if( (n-i) % i == 0):
        result += 1
    i += 1

print(result)