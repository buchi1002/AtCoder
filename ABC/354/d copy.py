def f(X, Y):
    S = (X//4)*(Y//2)*8
    if X%4 == 0:
        if Y%2 == 0:
            pass
        else:
            S += 4*(X//4)
    elif X%4 == 1:
        if Y%2 == 0:
            S += 3*(Y//2)
        else:
            S += 2 + 4*(X//4) + 3*(Y//2)
    elif X%4 == 2:
        if Y%2 == 0:
            S += 6*(Y//2)
        else:
            S += 3 + 4*(X//4) + 6*(Y//2)
    elif X%4 == 3:
        if Y%2 == 0:
            S += 7*(Y//2)
        else:
            S += 3 + 4*(X//4) + 7*(Y//2)
    return S


A, B, C, D = map(int, input().split())
width = C-A
height = D-B

A %= 4
B %= 2
C = A + width
D = B + height

print(f(C, D) - f(C, B) - f(A, D) + f(A, B))
