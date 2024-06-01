from collections import defaultdict
def main():
    d = defaultdict(lambda:100000000000)
    N = int(input())

    for _ in range(N):
        a, c = map(int, input().split())
        d[c] = min(d[c], a)

    print(max([a for a in d.values()]))
main()
