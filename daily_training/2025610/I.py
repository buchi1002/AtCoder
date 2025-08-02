mod = 998244353
from collections import defaultdict
S = input()
d = defaultdict(lambda:0)

for s in S:
    d[s] += 1

