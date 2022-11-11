from collections import defaultdict

def main():
    N, X, Y = map(int, input().split())
    As = tuple(map(int, input().split()))

    dpx = [[False]*(2*10000+100) for _ in range(N//2 + N%2)]
    dpx[0][As[0]] = True
    dpy = [[False]*(2*10000+100) for _ in range(N//2)]
    dpy[0][As[1]] = True
    dpy[0][-As[1]] = True
    idx = 0
    idy = 0
    for i in range(2, N):
        if i%2 == 0:
            idx += 1
            for x in range(-10**4, 10**4+1):
                dpx[idx][x] = (dpx[idx-1][x - As[i]] or dpx[idx-1][x + As[i]])

        else:
            idy += 1
            for y in range(-10**4, 10**4+1):
                dpy[idy][y] = (dpy[idy-1][y - As[i]] or dpy[idy-1][y + As[i]])


    if dpx[-1][X] and dpy[-1][Y]:
        print("Yes")
    else:
        print("No")

main()
