def main():
    # input
    N = int(input())
    # compute

    # output
    N = int(N*1.08)
    if N < 206:
        print('Yay!')
    elif N == 206:
        print('so-so')
    else:
        print(':(')
if __name__ == '__main__':
    main()
