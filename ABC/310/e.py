N = int(input())
Ss = [int(s) for s in input()]

dp = [[0, 0] for _ in range(N)]
dp[0][Ss[0]] += 1

for i in range(1, N):
    dp[i][Ss[i]] += 1
    if Ss[i] == 0:
        dp[i][1] += (dp[i-1][0] + dp[i-1][1])
    else:
        dp[i][0] += dp[i-1][1]
        dp[i][1] += dp[i-1][0]

print(sum([dp[i][1] for i in range(N)]))
