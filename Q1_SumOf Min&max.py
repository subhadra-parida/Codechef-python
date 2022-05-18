n=int(input("enter"))
s=list(map(int, input().split(',')))
i=0
while i<len(s):
     maximum=max(s) 
     minimum=min(s)
     i+=1
print((maximum)+(minimum))