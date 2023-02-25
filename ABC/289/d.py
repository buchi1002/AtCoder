N = int(input())
As = list(map(int,input().split()))
M = int(input())
Bs = set(map(int,input().split()))
X = int(input())

dp = [False]*(X+1)
dp[0] = True
for step in range(X):
    if dp[step] and (step not in Bs):
        for i in range(N):
            if (step + As[i] <= X):
                dp[step + As[i]] = True

if dp[X]:
    print("Yes")
else:
    print("No")
