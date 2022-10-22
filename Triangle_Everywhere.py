a,b,c=map(int,input().split())
if a+b > c and b+c > a and a+c > b:
    if a==b and  b==c:
        print('1')
    elif a==b or b==c or c==a:
        print('2')
    else:
        print('3')
else:
    print('-1')


    