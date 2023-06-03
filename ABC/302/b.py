H, W = map(int, input().split())
Ss = [input() for _ in range(H)]

vec = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(H):
    for j in range(W):
        for v in vec:
            vx, vy = v
            if (0 <= j + vx*4 < W) and (0 <= i + vy*4 < H):
                S = ""
                for k in range(5):
                    S += Ss[i+vy*k][j+vx*k]
                if S == "snuke":
                    for p in range(5):
                        print(*[i+vy*p+1, j+vx*p+1])
