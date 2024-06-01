def d(P1, P2):
    X1, Y1 = P1
    X2, Y2 = P2

    return (X1-X2)**2 + (Y1-Y2)**2

N = int(input())
Ps = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    M = N-1
    v = -1
    for j in range(N-1, -1, -1):
        if i == j:
            continue
        if v <= d(Ps[i], Ps[j]):
            M = j
            v = d(Ps[i], Ps[j])

    print(M+1)
