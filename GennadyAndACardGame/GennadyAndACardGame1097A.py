card = input()
hand = input().split(" ")
flag = False

for c in hand:
    if(c[0] == card[0] or c[1] == card[1]):
        flag = True

print("YES") if flag else print("NO")

