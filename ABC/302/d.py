N, M, D = map(int, input().split())
As = sorted(map(int, input().split()))
As.reverse()
Bs = sorted(map(int, input().split()))
Bs.reverse()


idx_a = 0
idx_b = 0

while True:
    if abs(As[idx_a] - Bs[idx_b]) <= D:
        print(As[idx_a]+Bs[idx_b])
        break
    else:
        if As[idx_a] > Bs[idx_b]:
            idx_a += 1
            if idx_a == N:
                print(-1)
                break
        else:
            idx_b += 1
            if idx_b == M:
                print(-1)
                break
