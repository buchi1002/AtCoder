def main():
    N, K = input().split()
    N = int(N)
    Kr = str(int(K[::-1]))
    Kc = str(int(Kr[::-1]))

    if K != min(Kr, Kc):
        print(0)

    else:
        K = int(K)
        Kr = int(Kr)

        S = set([])
        while K <= N:
            S.add(K)
            K *= 10

        while Kr <= N:
            S.add(Kr)
            Kr *= 10

        print(len(S))

if __name__ == '__main__':
    main()
