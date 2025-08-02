from itertools import combinations
def rec(G:list[list], seen:list[bool], key:int, l, m):
    if seen[key]:
        return
    seen[key] = True
    m[0] = max(m[0], l)
    for k in G[key]:
        rec(G, seen, k, l + 1, m)
    seen[key] = False

N, M = map(int, input().split())
Ss = [input() for _ in range(N)]
G = [list() for _ in range(N)]
for i, j in combinations(range(N), 2):
    if 1 ==sum(1 for k in range(M) if Ss[i][k] != Ss[j][k]):
        G[i].append(j)
        G[j].append(i)

m = [1]
for i in range(N):
    seen = [False] * N
    rec(G, seen, i, 1, m)

if m[0] == N:
    print("Yes")
else:
    print("No")
