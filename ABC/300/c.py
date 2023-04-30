def main():
    H, W = map(int, input().split())
    Cs = list()
    for i in range(H):
        Cs.append(input())

    Ss = [0]*(min(H, W)+10)
    for i in range(H):
        for j in range(W):
            if Cs[i][j] == "#":
                for d in range(1,max(H, W)):
                    if (i+d < H and i-d >= 0 and j+d < W and j-d >= 0) and (Cs[i+d][j+d] == Cs[i+d][j-d] == Cs[i-d][j+d] == Cs[i-d][j-d] == "#"):
                        pass
                    else:
                        Ss[d] += 1
                        break
    print(*Ss[2:(min(H,W)+2)])

main()
