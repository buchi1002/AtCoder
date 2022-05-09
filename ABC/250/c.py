def main():
    N, Q = map(int, input().split())
    Xs = [int(input()) for _ in range(Q)]
    As = [[i-1,i+1] for i in range(N+10)]

    for i in range(Q):
        if As[Xs[i]][1] != N+1:
            N1 = As[Xs[i]][0]
            N2 = Xs[i]
            N3 = As[Xs[i]][1]
            N4 = As[N3][1]

            As[N1][1] = N3
            As[N2] = [N3, N4]
            As[N3] = [N1, N2]
            As[N4][0] = N2
        else:
            N1 = As[As[Xs[i]][0]][0]
            N2 = As[N1][1]
            N3 = As[N2][1]
            N4 = As[N3][1]

            As[N1][1] = N3
            As[N2] = [N3, N4]
            As[N3] = [N1, N2]
            As[N4][0] = N2
    s = ""
    for i in range(N):
        if i == 0:
            L = As[0][1]
            s += str(L)
        else:
            L = As[L][1]
            s += " " + str(L)
    print(s)

if __name__ == '__main__':
    main()
