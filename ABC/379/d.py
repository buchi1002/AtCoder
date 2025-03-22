from bisect import bisect_left
def main():
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    times = [0 for _ in range(Q)]
    syukaku = [0 for _ in range(Q)]
    num = [0 for _ in range(Q+1)]

    t = 0
    for i in range(Q):
        if queries[i][0] == 2:
            t += int(queries[i][1])
        times[i] = t

    last = Q+1
    for i in range(Q):
        if queries[Q-i-1][0] == 3:
            last = Q-i-1
        syukaku[Q-i-1] = last

    for i in range(Q):
        if queries[i][0] == 1:
            H = queries[i][1]
            num[syukaku[bisect_left(times, times[i]+H)]] += 1

    for i in range(Q):
        if queries[i][0] == 3:
            print(num[i])


main()
