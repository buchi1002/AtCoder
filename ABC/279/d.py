import math

A, B = map(int, input().split())

N = math.pow(A/(2*B), (2/3)) - 1

start = max(0, int(N-10))
end = max(int(N + 10),100)

m = math.inf

for i in range(start, end+1):
    m = min(A/math.sqrt(i+1) + B*i, m)

print(m)
