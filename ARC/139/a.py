def main():
    N = int(input())
    Ts = list(map(int, input().split()))

    As = [0]*N
    As[0] = 2**Ts[0]
    for i in range(1,N):
        if 2**Ts[i] > As[i-1]:
            As[i] = 2**Ts[i]
        elif 2**Ts[i] == As[i-1]:
            As[i] = 2**(Ts[i]+1) + 2**(Ts[i])
        else:
            b = bin(As[i-1])[2:]
            b = b[:(len(b)-Ts[i])]
            b = int(b,2)
            b = (b+1 + (b%2 != 0))
            b = bin(b)[2:]
            As[i] = int(b + "0"*Ts[i],2)
    print(As[N-1])

if __name__ == '__main__':
    main()
