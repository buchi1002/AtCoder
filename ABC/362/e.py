from collections import combinations
N = int(input())
As = tuple(map(int, input().split()))
ans = N

d = set()
for a1, a2 in combinations(As, 2):
    d.add(a2-a1)
