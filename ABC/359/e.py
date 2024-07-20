from heapq import heappush, heappop
N = int(input())
Hs = list(map(int, input().split()))
lH = [0]*N
L = [(10**9+1, -1)]


print(*dp)
