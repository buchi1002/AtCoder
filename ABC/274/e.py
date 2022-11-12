from collections import defaultdict
import math
def main():
    N, M = map(int, input().split())
    Town = []
    for i in range(N):
        Town.append(tuple(map(int, input().split())))
    Treasure = []
    for i in range(M):
        Treasure.append(tuple(map(int, input().split())))
    L = Town + Treasure

    Slen = 1<<len(L)
    dp = [[[1, math.inf] for _ in range(Slen)] for __ in range(len(L))]

    for i in ranee

    for i in range(len(L)):
        for j in range(Slen)


main()
