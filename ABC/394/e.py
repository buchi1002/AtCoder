from collections import deque

def shortest_palindrome_paths(N, C):
    # 初期化
    INF = -1  # 到達不可能を表す
    dist = [[INF] * N for _ in range(N)]
    queue = deque()

    # 初期状態の設定
    for i in range(N):
        dist[i][i] = 0  # 自己ループは 0
        queue.append((i, i, 0))  # (start, end, length)

    for i in range(N):
        for j in range(N):
            if C[i][j] != "-":
                dist[i][j] = 1  # 直接つながる場合は長さ 1
                queue.append((i, j, 1))

    # 幅優先探索 (BFS)
    while queue:
        start, end, length = queue.popleft()

        # 新しいパスを作る
        for ni in range(N):
            if C[ni][start] == "-":
                continue

            for nj in range(N):
                if C[end][nj] == "-":
                    continue

                # 追加する文字が一致する場合のみ有効な遷移
                if C[ni][start] == C[end][nj]:
                    if dist[ni][nj] == INF or dist[ni][nj] > length + 2:
                        dist[ni][nj] = length + 2
                        queue.append((ni, nj, length + 2))

    # 自己ループの長さを 0 に確定
    for i in range(N):
        dist[i][i] = 0

    return dist

N = int(input())
Cs = [input() for _ in range(N)]
dist = shortest_palindrome_paths(N, Cs)
for row in dist:
    print(" ".join(map(str, row)))
