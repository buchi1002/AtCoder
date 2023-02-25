N, M = map(int,input().split())
As = list()
for i in range(M):
    C = input()
    As.append(set(map(int,input().split())))

length = (1 << M)
count = 0
for i in range(length):
    b = bin(i)[2:].zfill(M)

    S = set()
    for idx in range(M):
        if b[idx] == "1":
            S |= As[idx]
    if len(S) == N:
        count += 1

print(count)
