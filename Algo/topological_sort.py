# (参考)https://output-zakki.com/topological_sort/

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
