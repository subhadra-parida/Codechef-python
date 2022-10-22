N=int(input())
A=list(map(int,input().split()))
new_list=[]
for i in range(1,N+1):
    new_list.append(A[-i])
for i in new_list:
    print(i,end=" ")

    