N, K = map(int,input().split())
As = list(map(int, input().split()))
As.sort()

v = As[0]
l_idx = 0
L = [[v]]
for i in range(1, N):
    if As[i] - As[i-1] == 1:
        L[-1].append(As[i])
    else:
        L.append(list())
        L[-1].append(As[i])


Ed = [1]
for i in range(1, 2*(10**5)+1):
    Ed[i] = i*Ed[-1]%998244353
