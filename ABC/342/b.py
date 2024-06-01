from collections import defaultdict
def main():
    N = int(input())
    Ps = list(map(int, input().split()))
    d = defaultdict(int)
    for i, p in enumerate(Ps):
        d[p] = i
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        if d[a] > d[b]:
            print(b)
        else:
            print(a)
main()
