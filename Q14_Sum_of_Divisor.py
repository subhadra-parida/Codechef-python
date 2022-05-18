def function():
    n=int(input("Enter any number="))
    c=0
    for i in range(1,n+1):
        if n%i==0:
           c=c+i
        else:
           pass
    print(c)
function()