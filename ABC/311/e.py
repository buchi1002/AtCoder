def main():
    H, W, N = map(int, input().split())
    G = [[True]*W for _ in range(H)]

    for i in range(N):
        a, b = map(int, input().split())
        G[a-1][b-1] = False

    cnt = [[0]*W for _ in range(H)]
    cnt[0][0] = int(G[0][0])

    for i in range(1, H):
        cnt[i][0] = cnt[i-1][0] + int(G[i][0])


    for j in range(1, W):
        cnt[0][j] = cnt[0][j-1] + int(G[0][j])

    for i in range(1, H):
        for j in range(1, W):
            cnt[i][j] = cnt[i][j-1] + cnt[i-1][j] - cnt[i-1][j-1] + int(G[i][j])

    dp = [[0]*W for _ in range(H)]

    for i in range(H):
        dp[i][0] = int(G[i][0])

    for j in range(W):
        dp[0][j] = int(G[0][j])

    for i in range(1,H):
        for j in range(1,W):
            if not G[i][j]:
                continue
            dp[i][j] += 1
            if dp[i-1][j-1] != 0:


main()
