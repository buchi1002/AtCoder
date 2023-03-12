
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def rec(key, G, s, seen):
    if seen[key]:
        return

    seen[key] = True
    s.add(key)

    for k in G[key]:
        rec(k, G, s, seen)

    return

N, M = map(int, input().split())
G = [list() for _ in range(N)]
G1 = [list() for _ in range(N)]

for _ in range(M):
    a,b,c,d = input().split()
    a, c = int(a), int(c)

    a,c = a-1, c-1
    G[a].append(c)
    G[c].append(a)
    G1[a].append(c)

seen = [False]*N
ans = [0, 0]
T = list()
for i in range(N):
    if not seen[i]:
        s = set()
        rec(i, G, s, seen)
        T.append(list(s))

for t in T:
    ecnt= 0
    for e in t:
        ecnt += len(G1[e])

    if ecnt == len(t):
        ans[0] += 1
    else:
        ans[1] += 1

print(*ans)
