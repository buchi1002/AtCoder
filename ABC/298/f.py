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

    R = -1
    RM = -1
    for r in Rs.keys():
        if Rs[r] >= RM:
            R = r
            RM = Rs[r]

    C = -1
    CM = -1
    for c in Cs.keys():
        if Cs[c] >= CM:
            C = c
            CM = Cs[c]

    print(Rs[R] + Cs[C] - grid[(R,C)])

    print(Rs[2], Rs[R])
    print(Cs[2], Cs[C])
main()
