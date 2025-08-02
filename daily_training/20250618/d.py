X, K = map(int, input().split())
z = len(str(X))
for i in range(K):
    Y_1 = (X // 10 ** (i + 1))*(10 ** (i + 1))
    Y_2 = (X // 10 ** (i + 1) + 1)*(10 ** (i + 1))
    if abs(Y_1 - X) >= abs(Y_2 - X):
        X = Y_2
    else:
        X = Y_1
print(X)