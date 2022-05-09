def main():
    # input
    N = int(input())
    As = list(map(str, input().split()))
    # compute
    def zero3(n: str):
        return n[-3:].zfill(3)

    bs = list(map(zero3, As))

    d = 0
    o = 0
    cs = [0]*100
    ds = [0]*100

    for i in range(len(bs)):
        b = bs[i]
        if int(b[0])%2 == 0:
            cs[int(b[-2:])] += 1
        else:
            ds[int(b[-2:])] += 1

    for i in range(100):
        cs[i] = (1/2)*cs[i]*(cs[i] -1)
        ds[i] = (1/2)*ds[i]*(ds[i]-1)

    s = int(sum(cs) + sum(ds))
    # output
    print(s)
if __name__ == '__main__':
    main()
