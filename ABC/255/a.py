def main():
    R, C = map(int, input().split())
    As = [[0,0] for i in range(2)]

    for i in range(2):
        As[i] = list(map(int, input().split()))

    print(As[R-1][C-1])

if __name__ == '__main__':
    main()
