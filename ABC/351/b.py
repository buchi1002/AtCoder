N = int(input())
As = [input() for _ in range(N)]
Bs = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if As[i][j] != Bs[i][j]:
            print(i+1, j+1)
