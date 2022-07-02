def main():

    N, X = map(int,input().split())
    As = [0]*N
    Bs = [0]*N
    for i in range(N):
        As[i],Bs[i] = map(int,input().split())

    dp = [[False]*(10000+10) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(X+1):
                if j >= As[i] and dp[i][j-As[i]] == 1:
                    dp[i+1][j] = True
                if j >= Bs[i] and dp[i][j-Bs[i]] == 1:
                    dp[i+1][j] = True

    f = dp[N][X]
    print("Yes"*f + "No"*(1-f))


if __name__ == '__main__':
    main()
