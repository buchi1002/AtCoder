from collections import defaultdict

def main():
    N = int(input())
    MAXD = defaultdict(lambda : [0,0])
    D = defaultdict(lambda : defaultdict(lambda: 0))
    PD = {}
    num = 0
    for i in range(N):
        m = int(input())
        for j in range(m):
            p,e = map(int,input().split())
            D[i][p] = e
            MAXD[p] = sorted(MAXD[p]+[e],key= lambda x:-x)[:2]


    S = set()
    for i in range(N):
        m = []
        for p in D[i]:
            if (MAXD[p][0] == D[i][p]) and (MAXD[p][1] != MAXD[p][0]):
                m += [str(p)]
        S.add(tuple(m))

    print(len(S))
if __name__ == '__main__':
    main()
