from collections import defaultdict
def main():
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [0]*Q
    Xq = []
    for i in range(Q):
        Xq =int(input())
        Xs[i] = [int(input()),1]

    for i in range(N):
        Xs += [[As[i],0]]

    Xs.sort()

    X = [[0,0] for i in range(Q)]
    s = 0
    cnt = 0
    for i in range(N):
        if Xs[i][1] == 0:
            s += Xs[i][0]
            cnt += 1
        else:
            X[i] = [s,cnt]
    maxs = s

    for i in range(Q):
        print(X*X[i][1])
if __name__ == '__main__':
    main()
