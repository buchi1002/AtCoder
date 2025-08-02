T = input()
N = int(input())
dp = [False] * (len(T) + 1)
dp[0] = True
for _ in range(N):
    q = list(map(int, input().split()))
    A = q[0]
    Ss = q[1:]
    for i in range(N):
        if True:
            pass