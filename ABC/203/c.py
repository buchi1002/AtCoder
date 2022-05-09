def main():
    # input
    N, K = map(int, input().split())

    A = list()
    B = list()
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # compute
    L = [0]*(10**9)
    for i in range(N):
        L[A[i]] += B[i]
    p = K
    c = 0
    for i in L:
        p = -1 + L[i]
        c += 1
        if p == 0:
            break
    #output
    print(c)
if __name__ == '__main__':
    main()
