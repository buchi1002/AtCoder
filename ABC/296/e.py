from collections import deque
def topological_sort(G, into_num):
    q = deque()
    V = len(G)
    for i in range(V):
        if into_num[i]==0:
            q.append(i)

    ans = list()
    while q:
        v = q.pop()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1
            if into_num[adj]==0:
                q.append(adj)

    return ans

def main():
    N = int(input())
    As = list(map(int, input().split()))
    G = [list() for i in range(N)]

    into_num = [0]*N
    for i in range(N):
       G[i].append(As[i]-1)
       into_num[As[i]-1] += 1

    a = set(topological_sort(G, into_num))
    if len(a) == N:
        print(1)
    else:
        print(N - len(a))

main()
