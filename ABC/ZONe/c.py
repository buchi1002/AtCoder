H, W = map(int, input().split())
A = list()

for i in range(H):
    A.append(list(map(int, input().split())))

B = [[0]*H for _ in range(W)]

for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for i in range(W):
    print(*B[i])
