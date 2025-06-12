import heapq

def dijkstra(G, num_node):
    node = [float('inf')] * num_node
    node[0] = 0

    node_name = []
    heapq.heappush(node_name, [0, 0])

    while len(node_name) > 0:
        _, min_point = heapq.heappop(node_name)
        
        for goal, cost in G[min_point]:
            if node[min_point] | cost < node[goal]:
                node[goal] = node[min_point] | cost
                heapq.heappush(node_name, [node[min_point] | cost, goal])

    return node

N, M = map(int, input().split())
G = [list()] * N
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u - 1].append((v - 1, w))
    G[v - 1].append((u - 1, w))
cost = dijkstra(G, N)
print(cost[-1])
