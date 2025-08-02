N = int(input())
As = list(map(int, input().split()))
K = int(input())
print(sum(1 for a in As if K <= a))