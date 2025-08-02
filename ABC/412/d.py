from itertools import product
N, M = map(int, input().split())
G = [[False]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1][b-1] = True
    G[b-1][a-1] = True

# まず次数でソート
# 多い辺を少ない辺にくっつける

# 多い辺をくっつけたら