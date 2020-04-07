t = int(input())
for i in range(t):
    case = input().split("_")
    if(case[-1][-1] == "o"):
        print("FILIPINO")
    elif(case[-1][-1] == "u"):
        print("JAPANESE")
    elif(case[-1][-1] == "a"):
        print("KOREAN")

