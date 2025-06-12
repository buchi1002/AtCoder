# mod L の各頂点にリストを用意して掛け算
from bisect import bisect_left
N, L = map(int, input().split())
ds = list(map(int, input().split()))
if L%3 != 0:
    print(0)
else:
    arc = L // 3
    points = [0 for _ in range(L)]
    loc = 0
    points[loc] = 1
    for i in range(N - 1):
        loc = (loc + ds[i])%L
        points[loc] += 1
    cnt = 0
    for a in range(arc):
        cnt += points[a] * points[(a + arc)%L] * points[(a + 2* arc)%L]
    
    print(cnt)