N, K = map(int, input().split())
As = list(map(int, input().split()))

print(*[a//K for a in As if a%K==0])