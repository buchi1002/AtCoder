def main():
    N, X = map(int, input().split())

    Ans = [X]
    Ns = list(range(N+1))
    del Ns[X]

    if X == (N//2 + 1) and (N%2 == 1):
        for i in range(1,(N//2)+1):
            Ans = Ans + [X-i,X+i]

    elif X == (N//2) and (N%2 == 0):
        f1 = 0
        f2 = -1
        for i in range(0,N-1):
            if i%2==0:
                f1 +=1
            f2 *= (-1)
            Ans = Ans + [X+f2*f1]

    elif X == ((N//2)+1) and (N%2 == 0):
        f1 = 0
        f2 = 1
        for i in range(0,N-1):
            if i%2==0:
                f1 +=1
            f2 *= (-1)
            Ans = Ans + [X+f2*f1]

    elif (N-1)%2 == 0:
        s = (N-1)//2
        f1 = 0
        f2 = -1
        for i in range(N-1):
            if i%2==0:
                f1 +=1
            f2 *= (-1)
            Ans = Ans + [Ns[s+f2*f1]]

    print(*Ans)
if __name__ == '__main__':
    main()
