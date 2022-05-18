def Anagram():
    input1=input()
    input2=input()
    count=0
    l=len(input2)
    for i in input1:
        if i in input2:
            count=count+1
        else:
            pass
    
    if count == l:
        print("YES")
    else:
        print("NO")
Anagram()