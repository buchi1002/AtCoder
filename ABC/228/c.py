def main():
    N, K= map(int, input().split())
    Ps = [[0]*3 for i in range(N)]

    for i in range(N):
        Ps[i] = list(map(int, input().split()))

    Sums = [0]*N
    dist = [N]*1202

    for i in range(N):
        s = sum(Ps[i])
        Sums[i] = s
        for k in range(s,1202):
            dist[k] -= 1

    for i in range(N):
        if dist[Sums[i]+300]+1 <= K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
