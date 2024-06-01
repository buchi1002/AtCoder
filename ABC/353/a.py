N = int(input())
Hs = list(map(int, input().split()))

ans = -1
for i in range(1, N):
    if Hs[0] < Hs[i]:
        ans = i+1
        break

print(ans)
