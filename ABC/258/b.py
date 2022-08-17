def main():
    N = int(input())
    As = [""]*N

    for i in range(N):
        As[i] = input()

    D = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    M = 0
    for d in D:
        for i in range(N):
            for j in range(N):
                s = ""
                y,x = i-d[0],j-d[1]
                for n in range(N):
                    y = (y + d[0])%N
                    x = (x + d[1])%N
                    s += (As[y][x])
                M = max(int(s),M)

    print(M)

if __name__ == '__main__':
    main()
