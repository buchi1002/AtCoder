from collections import defaultdict
N = int(input())
d = defaultdict(lambda : 0)

Maxi = -1
M = 0
for _ in range(N):
    s = input()
    d[s] += 1

    if d[s] > M:
        Maxi = s
        M = d[s]

    
print(Maxi)