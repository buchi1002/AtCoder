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
