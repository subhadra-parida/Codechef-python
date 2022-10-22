T=int(input())
for i in range(T):
    N1, N2, N3=map(int,input().split())
    if N1>N2 and N1>N3:
        print(N1)
    elif N2>N1 and N2>N3:
        print(N2)
    else:
        print(N3)
        
        
