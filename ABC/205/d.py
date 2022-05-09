import math
def main():
    # input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Ks = [0]*Q
    for i in range(Q):
        Ks[i] = int(input())
    # compute
    if As[0]<10**5+1:
        cs = [i for i in range(As[0])]
        cl = len(cs)

        d = As[0]
        a = 0
        while cl <= 10**5+1:
            if a <= len(As):
                if d == As[a]:
                    a += 1
                    As.append(math.inf)
                    while As[a-1] == As[a]:
                        a += 1
                        As.append(math.inf)
                    d += 1
                    continue
            cs.append(d)
            cl += 1
            d += 1
        # output
        for i in Ks:
            print(cs[i])
    else:
        for i in Ks:
            print(i)
if __name__ == '__main__':
    main()
