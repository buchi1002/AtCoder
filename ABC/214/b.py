def main():
    S,T = map(int, input().split())
    i, j, k = 0, 0, 0
    count = 0
    while i <= S:
        if (i*j*k <= T) and (i + j + k <= S):
            count += 1
        k += 1
        if k == S+1:
            k = 0
            j += 1
        if j ==S+1:
            j = 0
            i += 1
    print(count)
if __name__ == '__main__':
    main()
