from collections import deque
def topological_sort(G, indeg):
    q = deque()
    V = len(G)
    for i in range(V):
        if indeg[i]==0:
            q.append(i)

    ans = list()
    while q:
        if len(q) >= 2:
            flag[0] = False
            break
        v = q.pop()
        ans.append(v)
        for adj in G[v]:
            indeg[adj] -= 1
            if indeg[adj]==0:
                q.append(adj)

    return ans


N, M = map(int, input().split())
G = [list() for _ in range(N)]
indeg = [0]*N
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    indeg[y] += 1

flag = [True]
ans = topological_sort(G, indeg)

if flag[0] and len(ans) == N:
    s = list(range(1, N+1))
    s.sort(key = lambda x: ans[x-1])
    print("Yes")
    print(*s)
else:
    print("No")
