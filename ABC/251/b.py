def main():
    N, W = map(int, input().split())
    As = list(map(int, input().split()))

    dict = {}
    if N>=1:
        for i in range(N):
            c = As[i]
            if c <= W:
                dict[c] = 1

    if N >= 2:
        for i in range(N-1):
            for j in range(i+1,N):
                c = As[i]+As[j]
                if c <= W:
                    dict[c] = 1

    if N >= 3:
        for i in range(N-2):
            for j in range(i+1,N-1):
                for k in range(j+1,N):
                    c = As[i]+As[j]+As[k]
                    if c <= W:
                        dict[c] = 1

    print(len(dict))

if __name__ == "__main__":
    main()
