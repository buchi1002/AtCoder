import itertools
from collections import defaultdict

L = {180,186,189,191,218}

d = [set() for _ in range(200)]
for i in range(1,len(L)):
    for s in itertools.combinations(L,i):
        d[sum(s)%200].add(s)

print(d[166])
