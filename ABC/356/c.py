from itertools import chain,combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def main():
    N, M, K = map(int, input().split())
    IN = list()
    for _ in range(M):
        I = input().split()
        C = int(I[0])
        As = set(map(int, I[1:C+1]))
        R = I[-1]
        IN.append([C, As, R])


    cnt = 0
    for s in powerset(range(1,N+1)):
        x = set(s)
        flag = True
        for I in IN:
            C, As, R = I
            if R == "o":
                if len(As & x) < K:
                    flag = False
                    break
            else:
                if len(As&x)>= K:
                    flag = False
                    break
        cnt += flag

    print(cnt)
main()
