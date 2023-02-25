MOD = 10**9 + 7

H, W = map(int, input().split())
grid = list()
for y in range(H):
    grid.append(input())

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if grid[i][j] == ".":
            if i == 0:
                dp[0][j] = dp[0][j-1]
                continue
            if j == 0:
                dp[i][0] = dp[i-1][0]
                continue
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%MOD
print(dp[H-1][W-1])
