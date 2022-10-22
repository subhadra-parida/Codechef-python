T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if ((A+B)%2!=0) or ((A+C)%2!=0):
        print("YES")
    else:
        print("NO")
        