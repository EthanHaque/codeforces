# nk = input()
# nk = nk.split(" ")
# for i in range(len(nk)):
#     nk[i] = int(nk[i])
    

# for i in range(nk[1]):
#     if(nk[0] % 10 == 0):
#         nk[0] = nk[0] // 10
#     else:
#         nk[0] = nk[0] - 1

# print(nk[0])

inData = input().split(" ")
n, k = int(inData[0]), int(inData[1])

for i in range(k):
    if(n % 10 == 0):
        n //= 10
    else:
        n -= 1

print(n)


