import sys

sys.setrecursionlimit(10000000)

def rec(key, value):
    if key in S:
        return

    S.add(key)

    L[key] = value + P[key]

    for k in d[key]:
        rec(k, L[key])

    return

from collections import defaultdict

N, Q = map(int, input().split())

d = defaultdict(lambda:set())
for i in range(N-1):
    a, b = map(int,input().split())
    d[a].add(b)
    d[b].add(a)

P = [0]*(N+1)
for q in range(Q):
    p, x = map(int,input().split())
    P[p] += x

S = set()
L = [0]*(N+1)
rec(1, 0)

print(*L[1:])
