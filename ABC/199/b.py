def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    # compute
    # output
    print(max((min(Bs)-max(As) + 1), 0))
if __name__ == '__main__':
    main()
