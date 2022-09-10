def main():
    import math

    N, M = map(int,input().split())
    As = list(map(int,input().split()))
    dp = [[-math.inf]*(M+1) for i in range(N)]

    dp[0][0] = 0
    for i in range(N):
        dp[i][0] = 0

    dp[0][1] = As[0]
    for i in range(1,N):
        for j in range(1,M+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + As[i]*j)

    print(dp[N-1][M])
if __name__ == '__main__':
    main()
