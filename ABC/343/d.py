from collections import defaultdict
def main():
    N, T = map(int, input().split())
    d_point = defaultdict(lambda:0)
    d_d = defaultdict(lambda:0)
    for i in range(N):
        d_d[0] += 1
    s = set()
    s.add(0)
    for i in range(T):
        a, b = map(int, input().split())
        d_d[d_point[a]] -= 1
        if d_d[d_point[a]] == 0:
            s.discard(d_point[a])

        d_point[a] += b
        if d_d[d_point[a]] == 0:
            s.add(d_point[a])
        d_d[d_point[a]] += 1

        print(len(s))
main()
