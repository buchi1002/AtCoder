N, M = map(int, input().split())
if M == 1:
    print(1)
elif M > N**2:
    print(-1)
else:
    if M <= N:
        print(M)
    else:
        for i in range(N):
