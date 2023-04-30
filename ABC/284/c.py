N, M = map(int,input().split())
G = [list() for i in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

cnt = 0
seen = [False]*len(G)
for p in range(N):
    if not seen[p]:
        cnt += 1
        C1 = set(G[p])
        while len(C1) != 0:
            C2 = set()
            for key in C1:
                seen[key] = True
            for key in C1:
                for k in G[key]:
                    if not seen[k]:
                        C2.add(k)
            C1, C2 = C2, C1

print(cnt)
