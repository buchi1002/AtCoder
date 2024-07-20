from heapq import heappop, heappush
def bfs(G, s):
    d = [-1]*(len(G))
    queue = [(0, s)]
    while queue:
        r, key = heappop(queue)
        if d[key] != -1:
            continue
        d[key] = r
        for k in G[key]:
            if d[k] == -1:
                heappush(queue, (d[key] + 1, k))
    return d

import sys
sys.setrecursionlimit(100000000)

def rec(key, G, seen, path, end):
    if path[-1]==end:
        return
    if seen[key]:
        return
    seen[key] = True
    for k in G[key]:
        path.append(k)
        rec(k, G, seen, path, end)
        if path[-1] != end:
            path.pop()
        else:
            return
    return

def main():
    N = int(input())
    G = [list() for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)


    dic = bfs(G, 0)
    L = 0
    for i in range(N):
        if dic[L] < dic[i]:
            L = i
    path = [L]

    dicL = bfs(G, L)
    R = L
    for i in range(N):
        if dicL[R] < dicL[i]:
            R = i

    path = [L]
    seen = [False]*N
    rec(L, G, seen, path, R)

    c = path[N//2]
    dc = list()
    for k in G[c]:
        dc.append(list())
main()
