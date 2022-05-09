def main():
    # input
    N = int(input())
    Ts = list(map(int, input().split()))
    # compute
    Ts.sort(reverse = True)
    x = 0
    y = 0
    for i in range(N):
        if y + Ts[i] <= x:
            y += Ts[i]
        else:
            x += Ts[i]
    # output
    print(max(x, y))
if __name__ == '__main__':
    main()
