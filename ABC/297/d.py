A, B = map(int, input().split())
A, B = max(A, B), min(A, B)

cnt = 0
while A != B:
    if A%B != 0:
        cnt += A//B
        A, B = B, A%B
    else:
        cnt += (A//B -1)
        break
print(cnt)
