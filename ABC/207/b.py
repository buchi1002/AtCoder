def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    if B >= C*D:
        print(-1)
    else:
        i = 0
        X = A
        Y = 0
        while X > Y*D:
            X += B
            Y += C
            i += 1
        print(i)
    # output
if __name__ == '__main__':
    main()
