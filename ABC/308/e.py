from collections import defaultdict

def main():
    N = int(input())
    As = list(map(int,input().split()))
    S = input()
    dp = [defaultdict(lambda:0) for i in range(3)]

    for i in range(N):
        if S[i] == "M":
            dp[0][As[i]] += 1

        elif S[i] == "E":
            for m in dp[0].keys():
                dp[1][tuple(sorted([m, As[i]]))] += dp[0][m]

        else:
            for e in dp[1].keys():
                dp[2][tuple(sorted(list(e) + [As[i]]))] += dp[1][e]

    mex = 0
    for x in dp[2].keys():
        mex += min(set([0, 1, 2, 3]) - set(x))*dp[2][x]
    print(mex)

main()
