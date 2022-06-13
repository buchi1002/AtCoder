from collections import defaultdict

def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = sorted(As)

    D = defaultdict(lambda :defaultdict(lambda : 0))
    for i in range(N):
        key = i%K
        D[key][As[i]] += 1

    f = 0
    for i in range(N):
        key = i%K
        if D[key][Bs[i]] != 0:
            D[key][Bs[i]] -= 1
        else:
            f = 1

    print("Yes"*(1-f)+"No"*f)

if __name__ == '__main__':
    main()
