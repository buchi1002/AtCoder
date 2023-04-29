def rotate(Xs, N):
    Ys = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            Ys[i][j] = Xs[N-1-j][i]

    return Ys
def main():
    N = int(input())
    As = list()
    for i in range(N):
        As.append(list(map(int, input().split())))

    Bs = list()
    for i in range(N):
        Bs.append(list(map(int, input().split())))


    flag = False
    check = True
    for i in range(N):
        for j in range(N):
            if As[i][j] == 1:
                if Bs[i][j] != 1:
                    check = False
                    break
    if check:
        flag = True

    As = rotate(As, N)
    check = True
    for i in range(N):
        for j in range(N):
            if As[i][j] == 1:
                if Bs[i][j] != 1:
                    check = False
                    break
    if check:
        flag = True

    As = rotate(As, N)
    check = True
    for i in range(N):
        for j in range(N):
            if As[i][j] == 1:
                if Bs[i][j] != 1:
                    check = False
                    break
    if check:
        flag = True

    As = rotate(As, N)
    check = True
    for i in range(N):
        for j in range(N):
            if As[i][j] == 1:
                if Bs[i][j] != 1:
                    check = False
                    break
    if check:
        flag = True

    if flag:
        print("Yes")
    else:
        print("No")




main()
