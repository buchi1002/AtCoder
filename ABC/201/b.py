def main():
    # input
    N = int(input())
    # compute
    Ss = ['', '']
    Ts = [0, 0]
    for i in range(N):
        S, T = map(str, input().split())
        T = int(T)
        if T > Ts[1]:
            Ts[0] = Ts[1]
            Ss[0] = Ss[1]
            Ts[1] = T
            Ss[1] = S
        elif T > Ts[0]:
            Ts[0] = T
            Ss[0] = S
    # output
    print(Ss[0])
if __name__ == '__main__':
    main()
