import sys

H, W, X, Y = map(int,input().split())
Ss = list()
Ss.append("#"*(W+2))
for i in range(H):
    Ss.append("#" + input() + "#")

Ss.append("#"*(W+2))

if Ss[X][Y] == "#":
    print(0)
else:
    count = 1
    for i in range(X-1, -1, -1):
        if Ss[i][Y] == "#":
            break
        else:
            count += 1

    for i in range(X+1,H+1):
        if Ss[i][Y] == "#":
            break
        else:
            count += 1

    for i in range(Y-1, -1, -1):
        if Ss[X][i] == "#":
            break
        else:
            count += 1

    for i in range(Y+1,W+1):
        if Ss[X][i] == "#":
            break
        else:
            count += 1

    print(count)
