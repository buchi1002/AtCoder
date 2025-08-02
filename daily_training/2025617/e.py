N, X = map(int, input().split())
As = list(map(int, input().split()))
S = set(As)

if any((a + X in S) for a in As):
    print("Yes")
else:
    print("No")