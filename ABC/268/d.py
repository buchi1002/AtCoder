from collections import defaultdict

def main():
    F = [0]*30
    F[0] = 1
    for i in range(1,30):
        F[i] = F[i-1]*i

    N, M = map(int,input().split())
    D = defaultdict(lambda:set())

    Ss = [0]*N
    Ts = [0]*N
    for i in range(N):
        Ss[i] = input()

    for i in range(N):
        T = input()
        TT = T.split("_")
        if "" in TT:
            TT.remove("")
        if (len(TT)!=N):
            continue

        K = T.replace("_", "")
        D[K].add(T)

    num = 16 - len('_'.join(Ss))
    Flag = False
    for key in D.keys():
        Comb = F[N-1+num]//(F[num]*F[N-1])
        if len(D[key]) == Comb:
            continue
        else:
            S = set()
            for v in D[key]:
                for i in range(N):
                    v = v.split(S[i])
            Flag = True
    if Flag == False:
        print(-1)
if __name__ == '__main__':
    main()
