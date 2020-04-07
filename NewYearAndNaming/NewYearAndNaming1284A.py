sl, tl = map(int, input().split(" "))
s = input().split(" ")
t = input().split(" ")
q = int(input())
for i in range(q):
    qn = int(input())
    print(s[(qn-1)%sl] + t[(qn-1)%tl])