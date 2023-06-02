N, M = map(int,input().split())
As = list()
for _ in range(M):
    As.append(list(map(lambda x:int(x)-1,input().split())))

G = [[False]*N for i in range(N)]

for i in range(M):
    for x in range(N-1):
        G[As[i][x]][As[i][x+1]] = True
        G[As[i][x+1]][As[i][x]] = True

cnt = 0
for i in range(N-1):
    for j in range(i,N):
        cnt += G[i][j]

print(N*(N-1)//2 - cnt)
