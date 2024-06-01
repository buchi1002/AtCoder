N = int(input())
L = list()

d = [False]*N
for i in range(N):
    a,c = map(int, input().split())
    L.append((c, -a, i))

L.sort()
