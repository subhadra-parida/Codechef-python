N=int(input())
disnict = 0
number = []
for i in range(1, N+1):
    if N%i==0:
        number.append(i)
        disnict=disnict+1
print(disnict)
for j in number: 
    print(j, end=" ")
        
