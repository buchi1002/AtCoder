def main():
    N ,A, X, Y = map(int, input().split())
    if N > A:
        print((N-A)*Y+X*A)
    else:
        print(N*X)
if __name__ == '__main__':
    main()
