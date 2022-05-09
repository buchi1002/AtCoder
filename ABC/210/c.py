def main():
    N, K = map(int, input().split())
    Cs = list(map(int, input().split()))

    if K == 1:
        print(1)
    else:
        Vs = {}
        Variety = 0
        Vmax = 0
        num = 0
        Ns = [0]*(N)

        for i in range(K):
            if (Cs[i] in Vs) == False:
                Vs[Cs[i]] = num
                Variety += 1
                Ns[num] += 1
                num += 1
            else:
                Ns[Vs[Cs[i]]] += 1
        Vmax = Variety
        for i in range(K,N):
            if (Cs[i] in Vs) == False:
                Vs[Cs[i]] = num
                Variety += 1
                Ns[num] += 1
                num += 1
            else:
                Ns[Vs[Cs[i]]] += 1
            Ns[Vs[Cs[i-K]]] -= 1
            if Ns[Vs[Cs[i-K]]] == 0:
                Vs.pop(Cs[i-K])
                Variety -= 1
            if Vmax < Variety:
                Vmax = Variety
        print(Vmax)
if __name__ == '__main__':
    main()
