from collections import defaultdict
def main():
    N, M = map(int,input().split())

    D = defaultdict(lambda:set())
    for i in range(M):
        u, v = map(int,input().split())
        D[u].add(v)
        D[v].add(u)

    cnt =  0
    for a in range(1,N-1):
        for b in range(a+1,N):
            for c in range(b+1,N+1):
                if b in D[a] and c in D[a] and c in D[b]:
                    cnt += 1

    print(cnt)
if __name__ == '__main__':
    main()
