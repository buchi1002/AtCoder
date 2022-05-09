def main():
    # input
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # compute
    DA = [0]*N
    DBC =[0]*N
    for i in range(N):
        DA[A[i]-1] += 1


    for i in range(N):
        DBC[B[C[i]-1]-1] += 1

    s = 0
    for i in range(N):
        s += DA[i]*DBC[i]

    # output
    print(s)
if __name__ == '__main__':
    main()
