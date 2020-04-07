n = int(input())
result = []
i = 1
while( i*i <= n):
    if n % i == 0:
        result.append(i)
        if n//i != i: 
            result.append(n//i)
    i += 1

print(result)