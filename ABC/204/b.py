def main():
    # input
    N =int(input())
    As = list(map(int, input().split()))
    # compute
    s = 0
    for i in range(N):
        if As[i] >= 11:
            s += As[i]- 10
    # output
    print(s)
if __name__ == '__main__':
    main()
