N, M= map(int, input().split())
As = list(map(int, input().split()))
Ns = [0]*M

for _ in range(N):
    Xs = list(map(int, input().split()))
    for i in range(M):
        Ns[i] += Xs[i]


if all(Ns[i]>=As[i] for i in range(M)):
    print("Yes")
else:
    print("No")
