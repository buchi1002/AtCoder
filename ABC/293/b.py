N = int(input())
As = tuple(map(int, input().split()))

C = [True]*N

for i in range(N):
    if C[i]:
        C[As[i]-1] = False

X = list()

for i in range(N):
    if C[i]:
        X.append(i+1)

print(len(X))
print(*X)
