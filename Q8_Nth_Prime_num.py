a=int(input("enter any num="))
count=0
i=0
while count<a:
	f=0
	j=1
	while j<=i:
		if i%j==0:
			f=f+1
		j=j+1
	if f==2:
		x=i
		count=count+1
	i=i+1
print(x)




# O/P:-
# Position 5=11
