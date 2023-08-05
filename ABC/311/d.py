import sys
sys.setrecursionlimit(100000000)

def rec(key, Ss, seen, path, N, M):
    y, x = key

    if seen[y][x]:
        return

    seen[y][x] = True

    for k in connect((y, x), Ss, path, N, M):
        rec(k, Ss, seen, path, N, M)
    return

def connect(t, Ss, path, N, M):
    y, x = t

    c = list()
    # 下
    for i in range(1, N):
        if y+i+1 < N:
            if Ss[y+i][x] == ".":
                path[y+i][x] = True
            else:
                break
            if Ss[y+i+1][x] == "#":
                c.append((y+i, x))
                break

    # 上
    for i in range(1,N):
        if y-i-1 >= 0:
            if Ss[y-i][x] == ".":
                path[y-i][x] = True
            else:
                break
            if Ss[y-i-1][x] == "#":
                c.append((y-i, x))
                break
    # 右
    for j in range(1,M):
        if x+j+1 < M:
            if Ss[y][x+j] == ".":
                path[y][x+j] = True
            else:
                break
            if Ss[y][x+j+1] == "#":
                c.append((y, x+j))
                break
    # 左
    for j in range(1,M):
        if x-j-1 >= 0:
            if Ss[y][x-j] == ".":
                path[y][x-j] = True
            else:
                break
            if Ss[y][x-j-1] == "#":
                c.append((y, x-j))
                break

    return c

def main():
    N, M = map(int, input().split())

    Ss = [input() for i in range(N)]

    seen = [[False]*M for _ in range(N)]
    path = [[False]*M for _ in range(N)]

    path[1][1] = True

    rec((1, 1), Ss, seen, path, N, M)


    a = 0
    for i in range(N):
        for j in range(M):
            a += (path[i][j] != 0)

    print(a)

main()
