N=int(input())
odd_number=0
even_number=0
for i in range(1,N*2+1):
    if i%2!=0:
        odd_number+=i
    else:
        even_number+=i
print(odd_number,even_number)

