from bisect import bisect
from collections import defaultdict

def main():
    W, H = map(int, input().split())
    N = int(input())
    berry = [tuple(map(int, input().split())) for _ in range(N)]

    A = int(input())
    As = tuple(map(int, input().split()))

    B = int(input())
    Bs = tuple(map(int, input().split()))

    d = defaultdict(lambda:0)

    for x, y in berry:
        a = bisect(As, x)
        b = bisect(Bs, y)

        d[(a,b)] += 1

    M = 0
    m = N+1
    for key in d.keys():
        M = max(d[key], M)
        m = min(d[key], m)
    if len(d.keys()) != (A+1)*(B+1):
        m = 0
    print(m, M)

main()
