N, K = map(int, input().split())
Ds = list(map(str, input().split()))


f = 0
for i in range(K):
    if str(N).count(Ds[i]) != 0:
        f = 1
        break

while f != 0:
    f = 0
    N += 1
    for i in range(K):
        if str(N).count(Ds[i]) != 0:
            f = 1
            break

print(N)
