from collections import defaultdict

def main():
    K = int(input())

    p = 2
    d = defaultdict(lambda:0)
    while p**2 <= K+1000:
        if K%p == 0:
            d[p] += 1
            K //= p
        else:
            p += 1

    flag = False
    if K != 1:
        d[K] += 1

    M = 0
    for key in d.keys():
        i = 1
        x = i
        v = 0

        count = 0
        while v < d[key]:
            count += 1
            v += 1
            while x%key == 0:
                v += 1
                x //=key

            i += 1
            x = i


        M = max(M, key*count)

    print(M)

main()
