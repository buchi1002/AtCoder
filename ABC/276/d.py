from collections import defaultdict
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def main():

    d2 = defaultdict(lambda:-1)
    s2 = set()

    v = 1
    r = 0
    while v <= 10**9:
        d2[v] = r
        s2.add(v)

        v = v*2
        r += 1

    d3 = defaultdict(lambda:-1)
    s3 = set()

    v = 1
    r = 0
    while v <= 10**9:
        d3[v] = r
        s3.add(v)

        v = v*3
        r += 1

    d = defaultdict(lambda:-1)
    s = set()
    for key2 in d2.keys():
        for key3 in d3.keys():
            if key2*key3 <= 10**9:
                d[key2*key3] = (d2[key2] + d3[key3])
                s.add(key2*key3)

    N = int(input())
    As = list(map(int, input().split()))

    G = As[0]
    for i in range(1,N):
        G = GCD(G, As[i])

    ans = 0
    flag = True
    for i in range(N):
        As[i] = As[i]//G
        if As[i] in s:
            ans += d[As[i]]
        else:
            flag = False
            break

    if flag:
        print(ans)

    else:
        print(-1)
if __name__ == '__main__':
    main()
