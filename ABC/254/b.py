def main():
    N = int(input())
    As = [[0]*(i+1) for i in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                As[i][j] = 1
            else:
                As[i][j] = As[i-1][j-1]+As[i-1][j]

    [print(*As[i]) for i in range(N)]

if __name__ == '__main__':
    main()
