def main():
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    times = [0 for _ in range(Q)]
    last_syukaku = [0 for _ in range(Q)]
    num = [0 for _ in range(Q+1)]

    last = 0
    time = 0
    for i in range(Q):
        last_syukaku[i] = last
        if queries[i][0] == 3:
            last = i

    ruisekiwa = [0 for _ in range(Q)]
    for i in range(1, Q):
        ruisekiwa[i] = ruisekiwa[i-1]
        if queries[i-1][0] == 1:
            ruisekiwa[i] += 1

    for i in range(Q):
        if queries[i][0] == 3:
            syukaku[i]

main()
