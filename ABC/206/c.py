def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    # compute
    As = sorted(As)
    Cs = [0]*(len(As))
    j = 0
    s = 0
    for i in range(N):
        if As[s] == As[i]:
            Cs[j] += 1
        else:
            s = i
            j = j+1
            Cs[j] += 1
    C = sum(Cs)
    X = 0
    for i in Cs:
        C -= i
        X += i*(C)
    # output
    print(X)

if __name__ == '__main__':
    main()
