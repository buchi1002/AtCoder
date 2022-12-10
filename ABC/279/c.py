from collections import defaultdict

def main():
    H, W = map(int,input().split())
    Ss = list()
    Ts = list()

    for i in range(H):
        Ss.append(input())

    for i in range(H):
        Ts.append(input())

    dS = defaultdict(lambda : 0)
    for j in range(W):
        e = ""
        for i in range(H):
            e += Ss[i][j]
        dS[e] += 1

    dT = defaultdict(lambda : 0)
    S = set()
    for j in range(W):
        e = ""
        for i in range(H):
            e += Ts[i][j]
        dT[e] += 1
        S.add(e)

    flag = True
    for k in S:
        if dT[k] != dS[k]:
            flag = False

    if flag:
        print("Yes")
    else:
        print("No")
main()
