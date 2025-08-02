A, B, K =map(int, input().split())
p = 1
for cnt in range(10**8):
    if A * p>= B:
        print(cnt)
        break
    else:
        p *= K