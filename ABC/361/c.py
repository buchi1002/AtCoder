from collections import deque
N, K = map(int, input().split())
As = list(map(int, input().split()))
As.sort()

m = 10**20
for i in range(K+1):
    m = min(As[i+(N-K-1)]-As[i], m)
print(m)
