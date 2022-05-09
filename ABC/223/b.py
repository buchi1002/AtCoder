def main():
    S = input()
    N = len(S)

    min = S
    max = S

    if N == 1:
        print(min)
        print(max)
    else:
        for i in range(N):
            S = S[1:] + S[0]

            if min > S:
                min = S
            if max < S:
                max = S
        print(min)
        print(max)

if __name__ == '__main__':
    main()
