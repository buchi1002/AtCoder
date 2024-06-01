N, K = map(int, input().split())
As = list(map(int, input().split()))
As.reverse()

cnt = 0
while As:
    AT = 0
    cnt += 1
    while len(As) > 0 and AT + As[-1] <= K:
        AT += As.pop()
print(cnt)
