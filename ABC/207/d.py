import math
def arg(L):
    rad = math.atan2(L[1], L[0])
    if rad < 0:
        rad += math.pi
    return rad

def main():
    N = int(input())
    Ss = [[0, 0, 0, 0] for i in range(N)]
    Ts = [[0, 0, 0, 0]for i in range(N)]

    A,B = 0, 0
    for i in range(N):
        x,y = list(map(int, input().split()))
        Ss[i] = [x, y, 0, 0]
        A += x
        B += y
    meanS = [A/N, B/N]

    C, D = 0, 0
    for i in range(N):
        x,y = list(map(int, input().split()))
        Ts[i] = [x,y, 0, 0]
        C += x
        D += y
    meanT = [C/N, D/N]

    for i in range(N):
        Ss[i] = [Ss[i][0] - meanS[0], Ss[i][1] - meanS[1], 0, 0]
        Ts[i] = [Ts[i][0] - meanT[0], Ss[i][1] - meanT[1], 0, 0]

        Ss[i][2] = math.sqrt(Ss[i][0]**2 + Ss[i][1]**2)
        Ts[i][2] = math.sqrt(Ts[i][0]**2 + Ts[i][1]**2)

        Ss[i][3] = arg(Ss[i])
        Ts[i][3] = arg(Ts[i])

    Ss = sorted(Ss, key = lambda x : x[3])
    Ts = sorted(Ts, key = lambda x : x[3])

    print("Ss", Ss)
    print("Ts", Ts)

    SA = Ss[0][3]
    TA = Ts[0][3]

    flag = 0
    for i in range(N):
        Ss[i][3] -= SA
        Ts[i][3] -= TA
        if (Ss[i][2] - Ts[i][2])**2 > 0.01 or (Ss[i][3] -Ts[i][3])**2 > 0.01:
            flag = 1
            print(i, Ss[i][2], Ts[i][2],Ss[i][3], Ts[i][3],)
    if flag == 1:
        print("No")
    else:
        print("Yes")
if __name__ == '__main__':
    main()

#偏角をどうするか？
