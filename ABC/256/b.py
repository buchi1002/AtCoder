def main():
    N = int(input())
    As = list(map(int, input().split())
)
    Base = [0,0,0,0]
    P = 0
    for i in range(N):
        Base[0] = 1
        for j in range(3,-1,-1):
            if Base[j] == 1:
                Base[j] = 0
                if j + As[i] >= 4:
                    P += 1
                else:
                    Base[j+As[i]] = 1

    print(P)
if __name__ == '__main__':
    main()
