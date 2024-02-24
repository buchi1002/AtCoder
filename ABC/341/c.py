def main():
    H, W, N = map(int, input().split())
    t = input()
    T = [(0, 0)]
    for i in range(N):
        if t[i] == "L":
            T.append((T[-1][0], T[-1][1]-1))
        if t[i] == "R":
            T.append((T[-1][0], T[-1][1]+1))
        if t[i] == "U":
            T.append((T[-1][0]-1, T[-1][1]))
        if t[i] == "D":
            T.append((T[-1][0]+1, T[-1][1]))
    G = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            flag = True
            for y, x in T:
                if  not ((0 <= i+y < H and 0 <= j+x < W) and (G[i+y][j+x] ==".")):
                    flag = False
            cnt += flag

    print(cnt)
