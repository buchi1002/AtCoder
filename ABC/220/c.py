def main():
    N = int(input())
    As = list(map(int, input().split()))
    X = int(input())

    S = sum(As)

    L = X%S

    m = 0
    i = 0
    kou = 0
    while m + As[i] <= L:
        m += As[i]
        i = i+1
        i = i % N
        kou += 1

    print((X//S)*N + kou + 1)

if __name__ == '__main__':
    main()
