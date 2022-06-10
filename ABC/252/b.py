def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    max = 0
    for i in range(N):
        if As[i] >= max:
            max = As[i]

    f = 0
    for i in range(K):
        if As[Bs[i]-1] == max:
            f = 1

    if f ==0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
