def main():
    N = int(input())
    LR = [list(map(int, input().split())) for i in range(N)]
    LR.sort()

    C = [0]*(2*10**5+10)
    LB = LR[0][0]
    RB = LR[0][1]

    for i in range(LB,RB):
        C[i] = 1

    for i in range(1,N):
        LA = LR[i][0]
        RA = LR[i][1]

        if RB < LA:
            for i in range(LA,RA):
                C[i] = 1
        elif LA <= RB and RB < RA:
            for i in range(RB,RA):
                C[i] = 1
        LB = LA
        RB = RA

    f = 1
    for i in range(len(C)):
        if f == 1 and C[i] == 1:
            start = i
            f = 0
        if f == 0 and C[i] == 0:
            end = i
            print(*[start,end])
            f = 1

if __name__ == '__main__':
    main()
