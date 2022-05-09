import math
def main():
    N = int(input())
    Ss = list(map(int, input().split()))
    Ts = list(map(int, input().split()))

    m = 0
    for i in range(N):
        if Ts[m] >= Ts[i]:
            m = i

    Cs = [0]*N

    j = m - 1
    c = 0
    while c <= N-1:
        j += 1
        k = j - 1
        if j == N:
            j = 0
        if Ts[j] <= Ss[k] + Cs[k]:
            Cs[j] = Ts[j]
        else:
            Cs[j] = Ss[k] + Cs[k]
        c += 1
    for i in range(N):
        print(Cs[i])
if __name__ == '__main__':
    main()
