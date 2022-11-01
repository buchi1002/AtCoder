def f(a, b, c, d):
    Flag = 0

    if (a[0] - b[0])**2 + (a[1] - b[1])**2 == (a[0] - c[0])**2 + (a[1] - c[1])**2 == (d[0] - b[0])**2 + (d[1] - b[1])**2 == (c[0] - d[0])**2 + (c[1] - d[1])**2:
        if (a[0]-b[0])*(a[0]-c[0]) + (a[1]-b[1])*(a[1]-c[1]) == 0:
            Flag = 1

    return Flag



def main():
    Ss = []
    for _ in range(9):
        Ss.append(input())

    Ps = []
    for i in range(9):
        for j in range(9):
            if Ss[i][j] == "#":
                Ps.append((i,j))

    count = 0
    for d1 in range(len(Ps)-3):
        for d2 in range(d1+1, len(Ps)-2):
            for d3 in range(d2+1, len(Ps)-1):
                for d4 in range(d3+1, len(Ps)):
                    count += f(Ps[d1], Ps[d2], Ps[d3], Ps[d4])

    print(count)
if __name__ == '__main__':
    main()
