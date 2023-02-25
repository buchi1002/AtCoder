from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

def rec(key, S, dic, count):
    if S[key]:
        return
    S[key] = True

    for k in dic[key]:
        rec(k, S, dic, count)

    return

def main():
    N, M = map(int, input().split())

    d = [[] for _ in range(N+1)]

    cnt = [0]
    for i in range(M):
        a, b = map(int,input().split())
        d[a].append(b)

    ans = 0
    for i in range(1,N+1):
        seen = [False]*(N+1)
        rec(i, seen, d, cnt)

        ans += sum(seen)

    print(ans)

main()
