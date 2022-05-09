def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    As.sort()
    Bs.sort()

    n, m = 0, 0
    ans = abs(As[n]-Bs[m])
    while n <= N-1 and m <= M-1:
        ans = min(ans, abs(As[n]-Bs[m]))
        if As[n]>Bs[m]:
            m += 1
        else:
            n += 1
    print(ans)
if __name__ == '__main__':
    main()
