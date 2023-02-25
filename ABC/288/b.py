N, K = map(int,input().split())
Ss = list()

for i in range(N):
    Ss.append(input())

Ss = Ss[:K].copy()
Ss.sort()
for i in range(K):
    print(Ss[i])
