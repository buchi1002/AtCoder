def main():
    N = int(input())
    As = list(map(int, input().split()))

    r = list()
    for i in range(N):
        r.append(As[i])
        while len(r) >= 2 and r[-1] == r[-2]:
            x = r[-1]
            r.pop()
            r.pop()
            r.append(x+1)

    print(len(r))
main()
