N=int(input())
J=1
while J<=N:
    G=N-J
    while G>0:
        print(" ", end="")
        G-=1
    M=J
    i=1
    while i<=M:
        print("*",end="")
        i+=1
    print()
    J+=1

    