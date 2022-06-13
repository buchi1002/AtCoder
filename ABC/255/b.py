import math

def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Asset = set(As)

    Xs = [0]*N
    Ys = [0]*N
    dmax = 0
    for i in range(N):
        Xs[i], Ys[i] = map(int,input().split())
    for i in range(N):
        if i+1 not in Asset:
            INF = math.inf
            dmin = INF
            for j in As:
                d = (Xs[i]-Xs[j-1])**2 + (Ys[i]-Ys[j-1])**2
                dmin = min(dmin,d)
            dmax = max(dmax,dmin)

    print(math.sqrt(dmax))
if __name__ == '__main__':
    main()
