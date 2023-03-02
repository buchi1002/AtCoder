from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(G:list, s:int):
    INF = 10**15
    N = len(G)
    roads = [-1]*N

    cost = [INF] * N
    cost[s] = 0
    h = []
    heappush(h, (0, s))
    while h:
        d, pos = heappop(h)
        for edge, nxt, c in G[pos]:
            if cost[pos] + c < cost[nxt]:
                cost[nxt] = cost[pos] + c
                heappush(h, (d + cost[pos], nxt))
                roads[nxt] = edge

    return roads


def main():
    N, M = map(int, input().split())
    G = [list() for _ in range(N)]
    d = dict()
    for i in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        G[a].append((i+1, b, c))
        G[b].append((i+1, a, c))

    roads = dijkstra(G, 0)

    ans = set()
    for i in range(1, N):
        ans.add(roads[i])

    print(*ans)

main()
