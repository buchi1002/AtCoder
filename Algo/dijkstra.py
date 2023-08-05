from heapq import heappop, heappush

def dijkstra(G:list, s:int):
    INF = 10**100
    N = len(G)

    cost = [INF] * N
    cost[s] = 0
    h = []
    heappush(h, (0, s))
    while h:
        pos = heappop(h)[1]
        for nxt, c in G[pos]:
            if cost[pos] + c < cost[nxt]:
                cost[nxt] = cost[pos] + c
                heappush(h, (cost[nxt], nxt))

    return cost
