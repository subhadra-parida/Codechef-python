T=int(input("Enter any time="))
for i in range(T):
    N,M,K=map(int,input().split())
    Eikooc=M*K
    if Eikooc>=N:
        print("YES")
    else:
        print("NO")
        