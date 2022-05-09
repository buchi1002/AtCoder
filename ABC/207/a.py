def main():
    # input
    A, B, C = map(int, input().split())
    # compute

    # output
    print(A+B+C-min(A, B, C))
if __name__ == '__main__':
    main()
