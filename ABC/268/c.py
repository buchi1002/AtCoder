def main():
    N = int(input())
    Ps = list(map(int,input().split()))

    Ss = [0]*N
    for i in range(N):
        X0 = ((Ps[i] - i - 1) + N)%N
        X1 = ((Ps[i] - i) + N)%N
        X2 = ((Ps[i] - i + 1) + N)%N

        Ss[X0] += 1
        Ss[X1] += 1
        Ss[X2] += 1

    print(max(Ss))
if __name__ == '__main__':
    main()
