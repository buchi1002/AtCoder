N, K, X = map(int, input().split())
As = list(map(int, input().split()))
As.insert(K, X)
print(*As)
