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

N, M = map(int, input().split())
G = [list() for _ in range(N+M)]

for i in range(N):
    A = int(input())
    Ss = list(map(lambda x:int(x)-1, input().split()))
    for s in Ss:
        G[i].append(N+s)
        G[N+s].append(i)

d = bfs(G, N+0)[-1]
if d == -1:
    print(d)
else:
    print(d//2-1)
