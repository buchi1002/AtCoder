def main():
    # input
    N, K = map(int, input().split())
    # compute
    def twoN(a: int):
        if a%200 == 0:
            a = int(a/200)
        else:
            a = int(str(a) + "200")
        return a
    for i in range(K):
        N = twoN(N)
    # output
    print(N)
if __name__ == '__main__':
    main()
