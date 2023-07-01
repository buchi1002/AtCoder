from heapq import heappop, heappush

N, K = map(int, input().split())
As = sorted(map(int, input().split()))
m = min(As)

ans = []
H = [0]

for idx in range(K+1):
    h = heappop(H)
    while len(ans) != 0 and ans[idx-1] == h:
        h = heappop(H)

    ans.append(h)
    for i in range(N):
        v = h+As[i]
        heappush(H, v)


print(ans[K])

from collections import deque
def bfs(G, s):
    queue = deque([s])
    d = [-1]*(len(G))
    d[s] = 0
    while queue:
        key = queue.popleft()
        for k in G[key]:
            if d[k] == -1:
                d[k] = d[key] + 1
                queue.append(k)
    return d
