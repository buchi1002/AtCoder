def main():
    N = int(input())
    Ss =[input() for i in range(N)]

    Ls = [[0]*10 for i in range(10)]
    for i in range(N):
        for j in range(10):
            Ls[int(Ss[i][j])][j] += 1

    mintime = 1000000
    for i in range(10): # 数字iについて
        imax = -1 #数字iの最大重複
        loc = -1 #最大重複があった場所
        time = 0
        for j in range(10): # 場所について
            if Ls[i][j] == 0:
                continue
            if Ls[i][j] >= imax:
                p = imax
                imax = Ls[i][j]
                loc = j
            time = loc + (imax-1)*10
        mintime = min(mintime,time)
    print(mintime)


if __name__ == '__main__':
    main()
