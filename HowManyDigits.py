from ast import Num
from tokenize import Number


Number=int(input("Enter any number="))
N=str(Number)
if len(N)==1:
    print("1")
elif len(N)==2:
    print("2")
elif len(N)==3:
    print("3")
elif len(N)>=3:
    print("More than 3 digits")


