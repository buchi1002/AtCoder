def main():

    N, W = map(int,input().split())
    Ws = [0]*N
    Vs = [0]*N

    for i in range(N):
        Ws[i], Vs[i] = map(int,input().split())

    dp = [[10**13]*((10**5)+10) for i in range(N)]

    dp[0][0] = 0
    dp[0][Vs[0]] = Ws[0]

    for i in range(1,N):
        for v in range((10**5+10)):
            dp[i][v] = dp[i-1][v]

            if v - Vs[i] >= 0:
                dp[i][v] = min(dp[i][v], dp[i-1][v - Vs[i]] + Ws[i])

    V = 0
    for v in range((10**5+10)):
        if dp[N-1][v] <= W:
            V = v

    print(V)
main()
