from heapq import heappop, heappush

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

Q = []
vis = [-(N+1000)] * N
for _ in range(K):
    P, H = map(int, input().split())
    P -= 1
    heappush(Q, (-H, P))
    vis[P] = H

while Q:
    cost, now = heappop(Q)
    cost *= -1
    if vis[now] > cost:
        continue
    for nxt in G[now]:
        if vis[nxt] < cost-1 and cost > 0:
            vis[nxt] = cost-1
            heappush(Q, (-vis[nxt], nxt))

ans = []
for i, a in enumerate(vis):
    if a >= 0:
        ans.append(i+1)

print(len(ans))
print(*ans)
