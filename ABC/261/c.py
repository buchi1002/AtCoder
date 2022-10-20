from collections import defaultdict
def main():
    N = int(input())
    D = defaultdict(lambda : -1)
    for i in range(N):
        S = input()
        D[S] += 1
        if D[S] == 0:
            print(S)
        else:
            print(S + "(" + str(D[S]) + ")")



if __name__ == '__main__':
    main()
