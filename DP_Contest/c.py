N = int(input())
As = list()
Bs = list()
Cs = list()

for i in range(N):
    a, b, c = map(int,input().split())
    As.append(a)
    Bs.append(b)
    Cs.append(c)

dp = [[0,0,0] for i in range(N)]
dp[0] = [As[0], Bs[0], Cs[0]]

for i in range(1,N):
    dp[i][0] = max(dp[i-1][1] + As[i], dp[i-1][2] + As[i])
    dp[i][1] = max(dp[i-1][2] + Bs[i], dp[i-1][0] + Bs[i])
    dp[i][2] = max(dp[i-1][0] + Cs[i], dp[i-1][1] + Cs[i])

print(max(dp[N-1]))
