l=input()
l=list(l)
no_rep = sorted(list(set(l)))
for i in no_rep:
    print(i,end="")
    print(l.count(i),end="")
    