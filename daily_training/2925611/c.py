T = int(input())

for _ in range(T):
    N = int(input())
    As = list(map(int, input().split()))
    print(sum(1 for a in As if a%2 == 1))