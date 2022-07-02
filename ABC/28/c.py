def main():
    L = list(map(int,input().split()))
    NUMs = set([])
    for i in range(3,2**5):
        b = bin(i)[2:].zfill(5)
        if b.count("1") == 3:
            S = 0
            for j in range(5):
                S += L[j]*int(b[j])
            NUMs.add(-S)
    NUMs = sorted(list(NUMs))

    print(-NUMs[2])
if __name__ == '__main__':
    main()
