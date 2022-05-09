def main():
    N, K = map(int, input().split())

    Ks = []
    k = K
    l = 2
    while k != 1:
        if k%l == 0:
            k = k//l
            Ks.append(l)
        else:
            l = l + 1
        print(k)
    print(Ks)
if __name__ == '__main__':
    main()
