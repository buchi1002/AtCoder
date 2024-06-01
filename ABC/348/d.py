from collections import defaultdict
def connect(y, x, H, W, e, d, seen, As):
    L = set()
    if e > 0:
        if y - 1 >= 0 and (not seen[y-1][x][e-1 + d[(y-1,x)]]) and As[y-1][x] !="#":
            L.add((y-1, x, e-1 +  d[(y-1,x)]))
            d[(y-1, x)] = 0
            seen[y-1][x][e-1 +  d[(y-1,x)]] = True
        if x - 1 >= 0 and (not seen[y][x-1][e-1 + d[(y,x-1)]])  and As[y][x-1] !="#":
            L.add((y,x-1, e-1 + d[(y,x-1)]))
            d[(y,x-1)]=0
            seen[y-1][x][e-1 +  d[(y,x-1)]] = True
        if x + 1 < W and (not seen[y][x+1][e-1 + d[(y,x+1)]])  and As[y][x+1] !="#":
            L.add((y,x+1, e-1 + d[(y,x+1)]))
            d[(y,x+1)]=0
            seen[y-1][x][e-1 +  d[(y,x+1)]] = True
        if y + 1 < H and (not seen[y+1][x][e-1 + d[(y+1,x)]])  and As[y+1][x] !="#":
            L.add((y+1,x, e-1 + d[(y+1,x)]))
            d[(y+1,x)]=0
            seen[y-1][x][e-1 +  d[(y+1,x)]] = True
    return L

def main():
    H, W = map(int, input().split())
    As = [input() for _ in range(H)]

    d = defaultdict(lambda:0)
    N = int(input())
    for _ in range(N):
        R, C, E = map(int, input().split())
        d[(R-1, C-1)] = E

    for i in range(H):
        for j in range(W):
            if As[i][j] == "S":
                sy, sx = i, j
            if As[i][j] == "T":
                ty, tx = i, j

    seen = [[[False for i in range(H*W*H*W+1000)] for i in range(W)] for j in range(H)]

    e = d[(sy, sx)]
    seen[sy][sx][e] = True

    next = list()
    if e > 0:
        next = connect(sy, sx, H, W, e, d, seen, As)

    while len(next) != 0:
        c_next = set()
        for py, px, e in next:
            c_next |= connect(py, px, H, W, e, d, seen, As)
        c_next, next = next, c_next
    f = False
    for e in range(H*W*H*W+1000):
        f = f or seen[ty][tx][e]

    if f:
        print("Yes")
    else:
        print("No")



main()
