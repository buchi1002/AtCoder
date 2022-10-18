def main():
    N, S = map(int,input().split())
    As = [0]*N
    Bs = [0]*N
    for i in range(N):
        As[i], Bs[i] = map(int,input().split())

    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(S):
            if dp[i][j] == 1:
                if j + As[i] <= S:
                    dp[i+1][j + As[i]] = 1
                if j + Bs[i] <= S:
                    dp[i+1][j + Bs[i]] = 1

    if dp[N][S] == 0:
        print("No")
    else:
        v = S
        ans = ""
        for i in range(N, 0, -1):
            if v - As[i-1] >= 0 and dp[i-1][v - As[i-1]] == 1:
                ans = "H" + ans
                v -= As[i-1]
            else:
                ans = "T" + ans
                v -= Bs[i-1]
        print("Yes")
        print(ans)
if __name__ == '__main__':
    main()
