string1=input("Enter any number=")
string2=input("Enter any thing=")
i=0
while i<len(string1):
    if string2 in string1:
        print("Yes")
        break
    else:
        print("No")
        break
    i=i+1