N = int(input())
As = list(map(int, input().split()))

if all(As[i+1] == As[i] for i in range(N-1)):
    print("Yes")
else:
    print("No")