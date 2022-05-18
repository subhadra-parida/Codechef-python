def pal(a):
    s=''
    i=len(a)-1
    while i>=0:
       s=s+a[i]
       i=i-1
       if (s==a):
          return "is palindrome"  
print(pal("LEVEL"))
