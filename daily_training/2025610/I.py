mod = 998244353
from collections import defaultdict
S = input()
d = defaultdict(lambda:0)

for s in S:
    d[s] += 1

ans = 1
for i in range(1, len(S) + 1):
    ans = (ans * i) % mod

for v in d.values():
    for i in range(1, v + 1):
        ans = (ans * pow(v, -1, mod)) % mod

print(ans)