def main():
    mod = 998244353
    N = int(input())

    c = N
    check = True
    c2 = 0
    c3 = 0
    c5 = 0
    while c != 1:
        x = False
        if c%2 == 0:
            c //= 2
            c2 += 1
            x = True
        if c%3 == 0:
            c //= 3
            c3 += 1
            x = True
        if c%5 == 0:
            c //= 5
            c5 += 1
            x = True
        if not x:
            if c != 1:
                check = False
                break

    inv5 = pow(5, -1, mod)
    if not check:
        print(0)
    else:
        dp = [[[0 for k in range(c5+1)] for j in range(c3+1)] for i in range(c2+1)]
        dp[0][0][0] = 1
        for i in range(c2+1):
            for j in range(c3+1):
                for k in range(c5+1):

                    if i - 1 >= 0:
                        dp[i][j][k] += inv5*(dp[i-1][j][k])
                    if j - 1 >= 0:
                        dp[i][j][k] += inv5*(dp[i][j-1][k])
                    if i - 2>= 0:
                        dp[i][j][k] += inv5*(dp[i-2][j][k])
                    if k - 1>= 0:
                        dp[i][j][k] += inv5*(dp[i][j][k-1])
                    if i - 1>= 0 and j - 1 >= 0:
                        dp[i][j][k] += inv5*(dp[i-1][j-1][k])

                    dp[i][j][k] %= mod

        print(dp[c2][c3][c5])





main()
