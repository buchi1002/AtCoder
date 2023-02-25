N, W = map(int,input().split())
Ws = [0]*N
Vs = [0]*N

for i in range(N):
    Ws[i], Vs[i] = map(int,input().split())

dp = [[0]*(W+1) for _ in range(N)]

dp[0][0] = 0
dp[0][Ws[0]] = Vs[0]

for i in range(1, N):
    for w in range(W+1):
        dp[i][w] = dp[i-1][w]

        if w - Ws[i] >= 0:
            dp[i][w] = max(dp[i][w], dp[i-1][w - Ws[i]] + Vs[i])

print(max(dp[N-1]))
