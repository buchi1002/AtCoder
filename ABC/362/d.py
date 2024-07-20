from heapq import heappop, heappush
def bfs(G, s, As):
    d = [-1]*(len(G))
    queue = [(As[s], s)]
    while queue:
        r, key = heappop(queue)
        if d[key] != -1:
            continue
        d[key] = r
        for b, k in G[key]:
            if d[k] == -1:
                heappush(queue, (d[key] + As[k] + b, k))
    return d

N, M = map(int, input().split())
As = list(map(int, input().split()))
G = [list() for _ in range(N)]
for _ in range(M):
    u, v, b = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((b, v))
    G[v].append((b, u))

ans = bfs(G, 0, As)
print(*ans[1:])
