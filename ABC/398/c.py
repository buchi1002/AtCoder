from collections import defaultdict
N = int(input())
As = list(map(int, input().split()))
Xs = [[As[i], i+1] for i in range(N)]
Xs.sort(key = lambda x:-x[0])

flag = True
for i in range(N-1):
    if i != 0:
        if Xs[i-1][0] == Xs[i][0]:
            continue

    if Xs[i][0] == Xs[i+1][0]:
        continue
    else:
        print(Xs[i][1])
        flag = False
        break

if flag:
    if N == 1:
        print(1)
    elif Xs[N-2][0] != Xs [N-1][0]:
        print(Xs[N-1][1])
    else:
        print(-1)
