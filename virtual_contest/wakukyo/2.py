H, W = map(int, input().split())
Ss = [input() for _ in range(H)]

for i in range(H):
    ans = list()
    for j in range(W):
        cnt = 0
        for iy in (y for y in range(-1, 1 + 1) if 0 <= i + y < H):
            for jx in (x for x in range(-1, 1 + 1) if 0 <= j + x < W):
                if Ss[i + iy][j + jx] == "#":
                    cnt += 1
        if Ss[i][j] == "#":
            cnt = "#"
        ans.append(str(cnt))
    print("".join(ans))
