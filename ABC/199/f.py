def main():
    # input
    A, B, C = map(int, input().split())
    # compute

    # output
    D = A**2 +B**2 - C**2
    if D >= 0:
        print("No")
    else:
        print("Yes")
if __name__ == '__main__':
    main()
