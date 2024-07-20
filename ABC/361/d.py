from collections import deque
def bfs(G, s):
    queue = deque([s])
    d = [-1]*(len(G))
    d[s] = 0
    while queue:
        key = queue.popleft()
        for c, k in G[key]:
            if d[k] == -1:
                d[k] = d[key] + c
                queue.append(k)
    return d

def main():
    N = int(input())
    G = [list() for _  in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        G[a].append((c, b))
        G[b].append((c, a))

    d0 = bfs(G, 0)
    s = 0
    for i in range(N):
        if d0[i] > d0[s]:
            s = i

    d1 = bfs(G, s)
    t = s
    for i in range(N):
        if d1[i] > d1[t]:
            t=i
    ans = 0
    for X in G:
        ans += sum(Xi[0] for Xi in X)
    print(ans-d1[t])
main()
