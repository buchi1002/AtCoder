def main():
    F = 2**30-1
    N, C = map(int,input().split())
    S = [0,0]*(N+1)
    S[0] = [2,F]
    X = C
    for i in range(N):
        T, A = map(int,input().split())
        if T == 1:
            F = F&A
            S[i] = [T,F]
        elif T == 2:
            F = F|A
            S[i] = [T,F]
        elif T == 3:
            X = X^A

if __name__ == '__main__':
    main()
