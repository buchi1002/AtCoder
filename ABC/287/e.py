from collections import defaultdict
def main():

    N = int(input())

    Ss = list()
    for i in range(N):
        s = input()
        Ss.append([s, i])

    Ss.sort()
    d = defaultdict(lambda:0)
    for i in range(1,N):
        b = Ss[i-1]
        a = Ss[i]
        v = 0
        for j in range(min(len(b[0]), len(a[0]))):
            if b[0][j] == a[0][j]:
                v += 1
            else:
                break
        d[b[1]] = max(d[b[1]], v)
        d[a[1]] = max(d[a[1]], v)


    for i in range(N):
        print(d[i])
main()
