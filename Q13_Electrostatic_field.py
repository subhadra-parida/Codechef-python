c=list(map(int, input().split()))
e=input()
l=int(input())
e=list(e)
count=0
for i in range(l):
    if e[i]=='P':
        count=count+c[i]
    else:
        count=count-c[i]
print(abs(count*100))

