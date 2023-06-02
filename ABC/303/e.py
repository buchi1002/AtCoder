from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)

def rec(key, G, seen, dist, d, L):
    if seen[key]:
        return

    if dist==0 and len(G[key]) >= 2:
        L.append(len(G[key]))
        dist = 3

    seen[key] = True
    for k in G[key]:
        rec(k, G, seen, dist-1, d, L)
    return

N = int(input())
G = [list() for _ in range(N)]
for i in range(N-1):
    u, v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

d = defaultdict(lambda:0)
seen = [False]*N
L = list()
for i in range(N):
    if len(G[i]) == 1:
        rec(i, G, seen, 1, d, L)

print(*sorted(L))
