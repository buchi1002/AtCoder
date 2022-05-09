def main():
    N, K = map(int, input().split())

    Basic = K//N
    Adv = K%N

    As = list(map(int, input().split()))

    Bs = sorted(As)

    if Adv == 0:
        for i in range(N):
            print(Basic)
    else:
        for i in range(N):
            if As[i] <= Bs[Adv-1]:
                print(Basic+1)
            else:
                print(Basic)


    print
if __name__ == '__main__':
    main()
