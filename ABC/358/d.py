def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    As.sort()
    Bs.sort()

    ANS = list()
    idx_a = 0
    for idx_b in range(M):
        while idx_a < N:
            if As[idx_a] < Bs[idx_b]:
                idx_a += 1
            else:
                ANS.append(As[idx_a])
                idx_a += 1
                break

    if len(ANS) == M:
        print(sum(ANS))
    else:
        print(-1)
main()
