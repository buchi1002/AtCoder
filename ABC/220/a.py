A, B, C = map(int, input().split())

k = 0
for i in range(2000000):
  if A <= C*i and C*i <= B:
    print(C*i)
    k = 1
    break

if k == 0:
    print(-1)
