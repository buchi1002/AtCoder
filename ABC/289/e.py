def check():
    N, M = map(int, input().split())
    Cs = tuple(map(int,input().split()))

    G = [list() for _ in range(N)]
    D = [[-1]*N for _ in range(N)]

    for m in range(M):
        u, v = map(int,input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    step = -1
    C = [[(0,N-1)], set()]

    C0 = C[0]
    C1 = C[1]

    seen = [[False]*N for _ in range(N)]
    while len(C0) != 0:
        step += 1
        for ta0, ao0 in C0:
            D[ta0][ao0] = step
            for ta1 in G[ta0]:
                for ao1 in G[ao0]:
                    if (not seen[ta1][ao1]) and Cs[ta1] != Cs[ao1]:
                        C1.add((ta1, ao1))
                        seen[ta1][ao1] = True
        C0, C1 = C1, C0
        C1 = set()

    print(D[N-1][0])


T = int(input())
for _ in range(T):
    check()
