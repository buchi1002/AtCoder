N, M = map(int,input().split())
As = tuple(map(int,input().split()))

Bs = list(range(1,N+1))

w_dic = dict()
for i in range(M):
    w_dic[i] = (Bs[As[i]-1], Bs[As[i]])
    Bs[As[i]-1], Bs[As[i]] = Bs[As[i]], Bs[As[i]-1]
loc = dict()
for i in range(N):
    loc[Bs[i]] = i+1


for i in range(M):
    if w_dic[i][0] != 1:
        if w_dic[i][1] != 1:
            print(loc[1])
        else:
            print(loc[w_dic[i][0]])
    else:
        print(loc[w_dic[i][1]])
