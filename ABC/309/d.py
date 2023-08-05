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


def main():
    N1, N2, M = map(int,input().split())
    G1 = [list() for _ in range(N1)]
    G2 = [list() for _ in range(N2)]

    for i in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1

        if a < N1:
            G1[a].append(b)
            G1[b].append(a)
        else:
            G2[a-N1].append(b-N1)
            G2[b-N1].append(a-N1)

    d1 = max(bfs(G1, 0))
    d2 = max(bfs(G2, N2-1))

    print(d1+d2+1)

main()
