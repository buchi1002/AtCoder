def main():
    # input
    import math
    R, X, Y = map(int, input().split())
    # compute
    D = math.sqrt(X**2+Y**2)
    if D%R == 0:
        print(int(math.sqrt(X**2+Y**2)/R))
    elif D <= 2*R:
        print(2)
    else:
        print((int((D//R + 1))))
    # output

if __name__ == '__main__':
    main()
