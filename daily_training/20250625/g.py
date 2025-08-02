def main():
    N, M = map(int, input().split())
    Cs = list(map(int, input().split()))
    K = list(9)
    As = list()
    for _ in range(M):
        l = list(map(int, input().split()))
        K.append(l[0])
        As.append(l[1:])
    
    from itertools import product
    for _ in product((0, 1), repa=2*N):
main()