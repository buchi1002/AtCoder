from collections import deque

N, M = map(int, input().split())
G = [list() for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))

seen = [[False] * (1 << 10) for _ in range(N)]

Z = 10**8
Q = deque()
Q.append((0, 0))

while len(Q) > 0:
    key, weight = Q.popleft()
    for k, w in G[key]:
        if not seen[k][weight ^ w]:
            seen[k][weight ^ w] = True
            Q.append((k, weight ^ w))
            if k == N - 1:
                Z = min(Z, weight ^ w)

print(Z if Z != 10**8 else -1)
