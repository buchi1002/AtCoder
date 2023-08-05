def rot(As, N):
    Xs = [[""]*N for _ in  range(N)]
    for j in range(1,N):
        Xs[0][j] = As[0][j-1]
        Xs[-1][j-1] = As[-1][j]

    for i in  range(1, N):
        Xs[i-1][0] = As[i][0]
        Xs[i][-1] = As[i-1][-1]

    for i in range(1, N-1):
        for j in range(1, N-1):
            Xs[i][j] = As[i][j]

    return Xs

N = int(input())
As = [input() for _ in range(N)]

Ans = rot(As, N)

[print("".join(Ans[i])) for i in range(N)]
