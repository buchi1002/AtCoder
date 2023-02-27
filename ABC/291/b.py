N = int(input())
Xs = list(map(int, input().split()))
Xs.sort()
print((sum(Xs[N:4*N]))/(3*N))
