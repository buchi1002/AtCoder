
N, Q = map(int, input().split())
G = [set() for i in range(N)]

cnt = N
for _ in range(Q):
    q = input()
    if q[0] == "1":
        _, u, v = map(int, q.split())
        cnt -= (len(G[u-1]) == 0) + (len(G[v-1]) == 0)
        G[u-1].add(v-1)
        G[v-1].add(u-1)
    else:
        _, v = map(int, q.split())
        for u in G[v-1]:
            G[u].remove(v-1)
            cnt += (len(G[u])==0)
        cnt += len(G[v-1]) != 0
        G[v-1] = set()


    print(cnt)
