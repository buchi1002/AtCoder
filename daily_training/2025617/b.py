N = int(input())
As = list(map(int, input().split()))

if any(As[i] == As[i+1] == As[i+2] for i in range(N-2)):
    print("Yes")
else:
    print("No")