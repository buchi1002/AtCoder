s = input()
t = input()

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


x, y = len(s), len(t)
ans = ""
while x != 0 and y != 0:
    if s[x-1] == t[y-1]:
        ans = s[x-1] + ans
        y -= 1
        x -= 1
    else:
        if dp[x][y-1] > dp[x-1][y]:
            y -= 1
        else:
            x -= 1

print(ans)
