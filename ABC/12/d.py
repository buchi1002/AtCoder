from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(G:list, s:int):
    INF = 1<< 60
    N = len(G)

    dist = [INF] * N
    dist[s] = 0
    q = [s]
    while q:
        pre = heappop(q)
        for nxt, cost in G[pre]:
            if dist[nxt] >= dist[pre] + cost:
                dist[nxt] = dist[pre] + cost
                heappush(q, nxt)

    return dist

def main():
    N, M = map(int, input().split())
    G = [list() for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a, b = a-1, b-1
        G[a].append((b, t))
        G[b].append((a, t))

    Min = 1 << 60
    for i in range(N-1):
        dist = dijkstra(G, i)
        Min = min(Min, max(dist))
    print(Min)
main()
