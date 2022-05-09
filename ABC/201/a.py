def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    X = max(A, B, C)
    Y = min(A, B, C)
    W = A + B + C - X -Y
    # output
    if X - W == W - Y:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
