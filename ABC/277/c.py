from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

def rec(loc):
    if loc in S:
        return

    S.add(loc)
    for l in d[loc]:
        rec(l)
    return

S = set()
N = int(input())

d = defaultdict(lambda:set())
for i in range(N):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

rec(1)


print(max(S))
