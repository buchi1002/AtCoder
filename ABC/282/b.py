import itertools

N, M = map(int,input().split())
Ss = list()

for _ in range(N):
    Ss.append(input())

count = 0
for a,b in itertools.combinations(range(N), 2):
    flag = True
    for p in range(M):
        if Ss[a][p] == "x" and Ss[b][p] == "x":
            flag = False
    if flag:
        count += flag

print(count)
