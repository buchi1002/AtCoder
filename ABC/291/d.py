mod  = 998244353

N = int(input())
As = list()
Bs = list()
for _ in range(N):
    a, b = map(int, input().split())
    As.append(a)
    Bs.append(b)

dp = [[0,0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1,N):
    if As[i-1] != As[i]:
        dp[i][0] = (dp[i][0] + dp[i-1][0])%mod
    if Bs[i-1] != As[i]:
        dp[i][0] = (dp[i][0] + dp[i-1][1])%mod
    if As[i-1] != Bs[i]:
        dp[i][1] = (dp[i][1] + dp[i-1][0])%mod
    if Bs[i-1] != Bs[i]:
        dp[i][1] = (dp[i][1] + dp[i-1][1])%mod

print(sum(dp[-1])%mod)
