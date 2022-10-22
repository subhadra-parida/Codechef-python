# T=int(input())
# for i in range(T):
#     X,Y=map(int,input().split())
#     if X>=Y:
#         print("YES")
#     else:
# #         print("NO")



# inp = list(map(int, input().split()))
# print(inp)
T=int(input())
for i in range(T):
    N=int(input())
    for j in range (N):
        A=list(map(int,input().split()))
        # A= list(map(int, input().split()))

        print(A)
        k=0
        sum=0
        while k<len(A):
            sum=sum+A[k]
            k=k+1
        print(sum)