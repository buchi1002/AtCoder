from itertools import permutations, combinations
def main():
    N = int(input())

    MG = int(input())
    G = [[False]*N for _ in range(N)]
    for _ in range(MG):
        u, v = map(int, input().split())
        G[u - 1][v - 1] = True
        G[v - 1][u - 1] = True

    MH = int(input())
    H = [[False]*N for _ in range(N)]
    for _ in range(MH):
        u, v = map(int, input().split())
        H[u - 1][v - 1] = True
        H[v - 1][u - 1] = True

    As = [[0]*N for _ in range(N)]
    for i in range(N - 1):
        Ai = list(map(int, input().split()))
        for j, a in enumerate(Ai):
            As[i][i + j + 1] = As[i + j + 1][i] = a
    
    mini = (10**6)*64 + 10
    for p in permutations(range(N)):
        cost = 0
        for u, v in combinations(range(N), 2):
            if G[u][v] != H[p[u]][p[v]]:
                cost += As[p[u]][p[v]]
        mini = min(cost, mini)
    print(mini)
main()