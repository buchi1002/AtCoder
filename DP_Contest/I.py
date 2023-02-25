N = int(input())
Ps = list(map(float, input().split()))
dp = [[0]*(N+1) for _ in range(N)]
dp[0][0] = 1 - Ps[0]
dp[0][1] = Ps[0]
for i in range(1,N):
    for j in range(N+1):
        dp[i][j] = dp[i-1][j-1]*Ps[i] + dp[i-1][j]*(1-Ps[i])

s = 0
point = N//2 + N%2
for i in range(point, N+1):
    s += dp[N-1][i]

print(s)
