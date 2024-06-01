from collections import defaultdict
S = input()
d = defaultdict(int)
for s in S:
    d[s] += 1


for i, s in enumerate(S):
    if d[s] == 1:
        print(i+1)
