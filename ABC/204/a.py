def main():
    # input
    x, y = map(int, input().split())

    # compute

    # output
    if x == y:
        print(x)
    else:
        l = [1, 1, 1]
        l[x] = 0
        l[y] = 0
        for i in range(3):
            if l[i] == 1:
                print(i)
if __name__ == '__main__':
    main()
