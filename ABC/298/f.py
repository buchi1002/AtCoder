from collections import defaultdict

def main():
    N = int(input())
    Rs = defaultdict(lambda:0)
    Cs = defaultdict(lambda:0)
    grid = defaultdict(lambda:0)
    for i in range(N):
        r, c, x = map(int, input().split())
        Rs[r] += x
        Cs[c] += x
        grid[(r,c)] = x

    S = -1
    for y, x in grid.keys():
        print(y, x, Rs[y], Cs[x], grid[(y, x)])
        if S < Rs[y] + Cs[x] - grid[(y, x)]:
            S = max(S, Rs[y] + Cs[x] - grid[(y, x)])

    print(S)

main()
