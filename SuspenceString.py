N = int(input())
for i in range(N):
    list = int(input())
    S = input()
    T = ""
    for j in range(list):
        # if list[i] % 2 == 0:
        if j%2==0:
            if S[0] == "0":
                T="0"+T
            else:
                T=T+"1"
            S = S[1:]
        else:
            if S[-1] == "0":
                T=T+"0"
            else:
                T="1"+T
            S = S[:-1]
    print(T)
