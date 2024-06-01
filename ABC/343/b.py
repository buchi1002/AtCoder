N = int(input())
As = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    ans = list()
    for j in range(N):
        if As[i][j] == 1:
            ans.append(j+1)
    print(*ans)
