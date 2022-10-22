T=int(input("Enter any time="))
for i in range (T):
    X,Y=map(int,input().split())
    N1=X*100
    N2=Y*10
    if N1<N2:
        print("Disposable")
    else:
        print("Cloth")

    