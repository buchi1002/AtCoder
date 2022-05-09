def main():
    # input
    N = int(input())
    S = str(input())
    Q = int(input())
    # compute
    Ts = [i for i in range(2*N)]
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            Ts[A-1], Ts[B-1] = Ts[B-1], Ts[A-1]
        else:
            Ts = Ts[N:] + Ts[:N]
    # output
    for i in range(2*N):
        print(S[Ts[i]], end = "")
if __name__ == '__main__':
    main()
