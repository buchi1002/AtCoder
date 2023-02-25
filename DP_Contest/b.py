N, K = map(int,input().split())
Hs = list(map(int, input().split()))
dp = [100000000000000000]*(N+10)
dp[0] = 0
for i in range(1, N):
    for k in range(1,K+1):
        if i - k < 0:
            continue
        dp[i] = min(dp[i], dp[i-k] + abs(Hs[i] - Hs[i-k]))

print(dp[N-1])
