def main():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))

    judge = [0]*(N+1)
    judge[X]=1
    j = As[X-1]
    count = 1

    while judge[j] == 0:
        count += 1
        judge[j] = 1
        j = As[j-1]

    print(count)

if __name__ == '__main__':
    main()
