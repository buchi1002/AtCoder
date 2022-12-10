from collections import defaultdict
def main():
    H, W, N, h, w = map(int,input().split())
    As = list()
    [As.append(list(map(int,input().split()))) for _ in range(H)]

    S = set()
    d = defaultdict(lambda:0)
    for i in range(H):
        for j in range(W):
            d[As[i][j]] += 1
            S.add(As[i][j])

    for i in range(h):
        for j in range(w):
            d[As[i][j]] -= 1
            if d[As[i][j]] == 0:
                S.discard(As[i][j])

    Ans = [[0]*(W-w+1) for _ in range(H-h+1)]
    Ans[0][0] = len(S)
    dir = 1
    idx_x = 0
    idx_y = 0
    while idx_y + (h-1) <= H-1:
        while 0 <= (idx_x + dir) and idx_x + dir + (w-1) <= W-1:
            idx_x += dir
            if dir == 1:
                for i in range(idx_y, idx_y + h):
                    d[As[i][idx_x - 1]] += 1
                    S.add(As[i][idx_x - 1])

                for i in range(idx_y, idx_y + h):
                    d[As[i][idx_x + (w-1)]] -= 1
                    if d[As[i][idx_x + (w-1)]] == 0:
                        S.discard(As[i][idx_x + (w-1)])
                Ans[idx_y][idx_x] = len(S)
            else:
                for i in range(idx_y, idx_y + h):
                    d[As[i][idx_x + w]] += 1
                    S.add(As[i][idx_x + w])

                for i in range(idx_y, idx_y + h):
                    d[As[i][idx_x]] -= 1
                    if d[As[i][idx_x]] == 0:
                        S.discard(As[i][idx_x])
                Ans[idx_y][idx_x] = len(S)

        if idx_y + (h-1) == H-1:
            break
        idx_y += 1

        for j in range(idx_x, idx_x + w):
            d[As[idx_y - 1][j]] += 1
            S.add(As[idx_y - 1][j])

        for j in range(idx_x, idx_x + w):
            d[As[idx_y + (h-1)][j]] -= 1
            if d[As[idx_y + (h-1)][j]] == 0:
                S.discard(As[idx_y + (h-1)][j])

        Ans[idx_y][idx_x] = len(S)
        dir = dir*(-1)

    [print(*Ans[i]) for i in range(len(Ans))]

main()
