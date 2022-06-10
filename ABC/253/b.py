def main():
    H, W = map(int, input().split())
    Ss = [input() for i in range(H)]

    loc1 = [0,0]
    loc2 = [0,0]
    flag = 0
    for i in range(H):
        for j in range(W):
            if Ss[i][j]=="o":
                if flag == 0:
                    loc1 = [i,j]
                    flag = 1
                else:
                    loc2 = [i,j]

    print(abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1]))
if __name__ == '__main__':
    main()
