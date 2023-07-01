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
