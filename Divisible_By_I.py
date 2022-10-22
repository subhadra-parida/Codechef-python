T= int(input("Enter any time="))
for i in range(T):
    N=int(input("Enter any  number="))
    P=1
    l=list()
    for i in range(N):
        if i%2:
            l.append(P)
            P=P+1
        else:
            l.append(N)
            N=N-1
            
    print(*l[::-1])   


