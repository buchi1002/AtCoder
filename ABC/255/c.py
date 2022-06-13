def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(int(A-X)))

    elif D > 0:
        if D*(N-1)+A <= X:
            print(X-(D*(N-1)+A))
        elif X <= A:
            print(A-X)
        else:
            r = (X-A)%D
            print(min(r,D-r))
    else:
        if X <= D*(N-1) + A:
            print((D*(N-1)+A)-X)
        elif A <= X:
            print(X-A)
        else:
            r = abs(X-A)%abs(D)
            print(min(r,abs(D)-r))
if __name__ == '__main__':
    main()
