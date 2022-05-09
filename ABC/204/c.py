import numpy as np

def main():
    # input
    N, M = map(int, input().split())
    Ls = np.eye(N)
    for i in range(M):
        A, B = map(int, input().split())
        Ls[A-1][B-1] = 1
    # compute
    c = 0
    for i in range(N):
        L = [0]*N
        R = [0]*N
        L[i] = 1
        Ls[i] =
    # output
    print(Ls[0])
if __name__ == '__main__':
    main()
