from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)

def rec(key, color, judge,Z, B, W, d):
    if not judge:
        return judge

    if key in B:
        if not color:
            judge = False
            return judge
        else:
            return judge
    elif key in W:
        if color:
            judge = False
            return judge
        else:
            return judge
    else:
        Z.add(key)
        if color:
            B.add(key)
        else:
            W.add(key)

    for k in d[key]:
        judge = judge and rec(k, not color, judge,Z, B, W, d)

    return judge


def main():
    N, M = map(int,input().split())
    d = defaultdict(lambda:set())
    for i in range(M):
        u,v = map(int,input().split())

        d[u].add(v)
        d[v].add(u)

    j = True
    count = 0
    res = N
    Z = set()
    Bs = list()
    Ws = list()
    for i in range(1,N+1):
        if i in Z:
            continue

        Bs.append(set())
        Ws.append(set())
        B = Bs[-1]
        W = Ws[-1]
        j = rec(i, True, j, Z, B, W, d)


        if not j:
            break

        res = res - len(B) - len(W)
        count += len(B)*len(W) + (len(B) + len(W))*res



    if not j:
        print(0)

    else:
        print(count - M)

main()
