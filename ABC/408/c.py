from heapq import heappop, heappush
N, M = map(int, input().split())
taiho = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
taiho.sort()
cnts = [0] * N
cnt = 0
ends = list()
for i in range(N):
    while len(taiho) > 0 and taiho[0][0] == i:
        l, r = heappop(taiho)
        cnt += 1
        heappush(ends, r)
    cnts[i] = cnt
    while len(ends) > 0 and ends[0] == i:
        heappop(ends)
        cnt -= 1

print(min(cnts))