X = list(map(int,input().split()))
X.sort()
A, B, C = X

x = A + B - C
if x < 0:
    print(-1)
else:
    print(C)
