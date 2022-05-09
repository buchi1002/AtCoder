def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    # compute
    sorted(As)
    x = [i for i in range(1, N+1)]
    # output
    if(sorted(As) == x):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
