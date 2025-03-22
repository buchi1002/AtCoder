N, T, P = map(int, input().split())
Ls = list(map(int, input().split()))
Ls.sort()

print(max(T-Ls[-P],0))
