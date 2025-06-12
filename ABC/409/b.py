N = int(input())
As = list(map(int, input().split()))
M = 1
for x in range(101):
    if sum(As[i] >= x for i in range(N)) >= x:
        M = x

print(M)