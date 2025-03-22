N = int(input())
Ss = [input() for _ in range(N)]

Ss.sort(key=lambda x: len(x))

print("".join(Ss))
