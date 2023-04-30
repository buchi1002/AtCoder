def main():
    H, W = map(int, input().split())
    As = list()
    for i in range(H):
        As.append(input())
    Bs = list()
    for i in range(H):
        Bs.append(input())

    exist = False
    for y in range(H):
        for x in range(W):
            flag = True
            for i in range(H):
                for j in range(W):
                    if As[(i+y)%H][(j+x)%W] != Bs[i][j]:
                        flag = False
            if flag:
                exist = True

    if exist:
        print("Yes")
    else:
        print("No")

main()
