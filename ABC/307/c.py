def main():
    HA, WA = map(int, input().split())
    As = list()
    for i in range(HA):
        As.append(input())

    HB, WB = map(int, input().split())
    Bs = list()
    for i in range(HB):
        Bs.append(input())

    HX, WX = map(int, input().split())
    Xs = list()
    for i in range(HX):
        Xs.append(input())

    flag = False
    W = 2*WA+2*WX+WB
    H = 2*HA+2*HX+HB
    for i in range(H-HA):
        for j in range(W-WA):
            C = [[False]*W for i in range(H)]
            for ia in range(HA):
                for ja in range(WA):
                    C[i+ia][j+ja] = As[ia][ja]

            for ib in range(HB):
                for jb in range(WB):
                    C[HA+HX+ib][WA+WX+jb] = C[WA+WX+ib][WA+WX+jb] or Bs[ib][jb]

            for ix in range()



    if flag:
        print("Yes")
    else:
        print("No")
