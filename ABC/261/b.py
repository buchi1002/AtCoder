def main():
    N = int(input())
    As = [input() for i in range(N)]

    D = {"W":-1,"L":1,"D":0}
    flag = 1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if D[As[i][j]] + D[As[j][i]] != 0:
                flag = 0

    print("correct"*flag + "incorrect"*(1-flag))

if __name__ == '__main__':
    main()
