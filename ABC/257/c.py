from collections import defaultdict

def main():
    N = int(input())
    T = input()
    Ws = list(map(int,input().split())
)
    Ls = sorted(Ws)
    Ls.append(max(Ls)+10)
    S = [0,0]*N

    L = [Ls[0]]
    for i in range(1,len(Ls)):
        if Ls[i-1] != Ls[i]:
            L.append(Ls[i])

    Wdict = defaultdict(lambda: [0,0])
    for i in range(N):
        if T[i] == "0":
            Wdict[Ws[i]][0] += 1
        else:
            Wdict[Ws[i]][1] += 1

    ans = 0
    ccnt = 0
    acnt = T.count("1")
    for x in L:
        c = Wdict[x][0]
        a = Wdict[x][1]

        ans = max(ans,ccnt + acnt)

        ccnt += c
        acnt -= a

    print(ans)


if __name__ == '__main__':
    main()
