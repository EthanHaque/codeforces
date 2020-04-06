n = input()
games = input()
A, D = games.count("A"), games.count("D")

if(A > D):
    print("Anton")
elif(D > A):
    print("Danik")
else:
    print("Friendship")