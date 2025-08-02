T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    x = a
    y = s - a
    print("Yes" if (x&y)==a and y >= 0 else "No")