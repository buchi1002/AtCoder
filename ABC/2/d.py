N, M = map(int,input().split())
D = {}
for i in range(N):
    D[i] = {i}

for i in range(M):
    x,y = map(int,input().split())
    D[x-1].add(y-1)
    D[y-1].add(x-1)
M = 0
for i in range(1,2**N):
    s = bin(i)[2:].zfill(N)
    Ms = set(list(range(N)))

    a = set([])
    for j in range(len(s)):
        if s[j] == "1":
            a.add(j)
            Ms &= D[j]
    Ms = Ms & a
    M = max(M,len(Ms))

print(M)
