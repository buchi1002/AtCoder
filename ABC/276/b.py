import bisect

def main():
    N, M = map(int, input().split())

    L = [[] for _ in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())

        bisect.insort(L[A], B)
        bisect.insort(L[B], A)

    for i in range(1, N+1):
        print(*([len(L[i])] + L[i]))

if __name__ == '__main__':
    main()
