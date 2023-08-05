import sys
sys.setrecursionlimit(100000000)


from itertools import combinations

def rec(key, G, seen):
    if seen[key]:
        return
    seen[key] = True
    for k in G[key]:
        rec(k, G, seen)
    return

N, T, M = map(int, input().split())

NG = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    NG[a-1].append(b-1)
    NG[b-1].append(a-1)

for ts in combinations(list(range(N)), T):
    Ts = [set() for _ in range(T)]
    for i in range(T):
        Ts[i].add(ts[i])
    for i in range(N):
