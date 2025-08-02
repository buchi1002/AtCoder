def main():
    N, H, M = map(int, input().split())
    dp0 = [-1]*(H + 1)
    dp0[H] = M
    Max = 0

    for i in range(N):
        a, b = map(int, input().split())
        # a
        dp1 = [-1]*(H + 1)
        Flag = False
        for h in range(H + 1):
            if (dp0[h] != -1) and ((h >= a) or (dp0[h] >= b)):
                Flag = True
                if h >= a:
                    dp1[h - a] = max(dp0[h], dp1[h - a])
                if dp0[h] >= b:
                    dp1[h] = max(dp0[h] - b, dp1[h])
        
        Max += Flag
        dp0, dp1 = dp1, dp0

    print(Max)

main()