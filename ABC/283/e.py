def flip(L):
    for i in range(len(L)):
        L[i] = 1 - L[i]

def main():
    H, W = map(int,input().split())
    As = list()
    for i in range(H):
        As.append(list(map(int, input().split())))

    Bs = [[False]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            check = list()
            if j - 1 >= 0:
                check.append(j-1)
            if j + 1 <= W-1:
                check.append(j+1)
            flag = False
            for c in check:
                if As[i][j] == As[i][c]:
                    flag = True
            Bs[i][j] = flag

    flag = True
    count = 0
    for i in range(H-1):
        flipflag = False
        for j in range(W):
            if Bs[i][j] == False:
                if As[i][j] != As[i+1][j]:
                    if i >= 1 and As[i][j] == As[i-1][j]:
                        continue
                    flip(As[i+1])
                    flipflag = True
                    count += 1
                    break
        if flipflag:
            for j in range(W):
                if Bs[i][j] == False:
                    if As[i][j] != As[i+1][j]:
                        if i >= 1 and As[i][j] == As[i-1][j]:
                            continue
                        flag = False
                        break
        if not flag:
            break

    if H == 1:
        for j in range(W):
            if Bs[0][j] == False:
                flag = False
    else:
        for j in range(W):
            if Bs[H-1][j] == False:
                if As[H-2][j] != As[H-1][j]:
                    flag = False

    if flag:
        print(min(count, min(H - count,count)))
    else:
        print(-1)

main()
