from collections import defaultdict
import sys

sys.setrecursionlimit(2000000)

def main():
    def rec(key,S):
        if count[1] == False:
            return
        if key in S:
            return
        S.add(key)

        count[0] += 1

        if count[0] > 10**6:
            count[1] = False
            return

        for k in d[key]:
            rec(k,S)

        S.discard(key)


    N, M = map(int,input().split())
    d = defaultdict(lambda:set())
    for _ in range(M):
        u,v = map(int,input().split())
        d[u].add(v)
        d[v].add(u)

    S = set()
    count = [0,True]
    rec(1,S)

    print(min(10**6,count[0]))

main()
