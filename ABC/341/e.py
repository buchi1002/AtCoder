def rev(left, right, L, R):
    pass
def judge(left, right, L, R):
    pass
def main():
    N, Q = map(int, input().split())
    S = input()
    left = [i for i in range(N)]
    right = [i for i in range(N)]
    for i in range(1, N):
        if S[i] != S[i-1]:
            left[i] = left[i-1]
        if S[-i-1] != S[-i]:
            right[-i-1] = right[-i]

    print(right)
    print(left)
    for _ in range(Q):
        q, L, R = map(int, input().split())
        if q == 1:
            rev(left, right, L, R)
        if q == 2:
            judge(left, right, L, R)
main()
