import sys
sys.setrecursionlimit(100000000)

def rec(key, G, seen, dp):
    if seen[key]:
        return dp[key]
    seen[key] = True
    for k in G[key]:
        dp[key] = max(dp[key], rec(k, G, seen, dp) + 1)
    return dp[key]

N, M = map(int, input().split())
G = [list() for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)

seen = [False]*N
dp = [0]*N
for i in range(N):
    rec(i, G, seen, dp)

print(max(dp))
