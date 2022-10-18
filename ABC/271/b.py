def main():
    N, Q = map(int,input().split())
    Ls = [tuple(map(int, input().split())) for _ in range(N)]

    for _ in range(Q):
        s, t = map(int,input().split())
        print(Ls[s-1][t])

if __name__ == '__main__':
    main()
