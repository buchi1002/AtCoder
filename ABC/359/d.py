from collections import deque
N, K = map(int, input().split())
S = input()

for i in range(len(S)-K):
    t = S[i:K]
