N, M = map(int,input().split())

if N*N < M:
    print(-1)
else:
    X = N**2
    for a in range(1, N+1):
        b = M//a + (M%a != 0)
        if a > b:
            break
        if b <= N:
            X = min(a*b, X)

    print(X)
