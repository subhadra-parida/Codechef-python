N=int(input())
R=1
for i in range(1,N+1):
    if i%2==1:
        print(R,R+1,R+2,R+3,R+4)
        R=R+5
    if i%2==0:
        print(R+4,R+3,R+2,R+1,R)
        R=R+5
    i=i+1
