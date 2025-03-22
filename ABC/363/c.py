def main():
    from itertools import permutations
    N, K = map(int, input().split())
    S = list(input())

    ans = set()
    for p in permutations(S):
        if all(p[i:i+K]!=p[i:i+K][::-1] for i in range(N-K+1)):
            ans.add(p)
    print(len(ans))

main()
