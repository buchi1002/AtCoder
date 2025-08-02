N, L, R = map(int, input().split())
cnt = 0
for i in range(N):
    x, y = map(int, input().split())
    if x <= L <= R <= y:
        cnt += 1

print(cnt)