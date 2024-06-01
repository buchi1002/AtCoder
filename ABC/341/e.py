def ren(row, index):
    if row[index] == index:
        return index
    else:
        ren(row, row[index])

def rev(left, right, L, R):
    if L != 0:
        if left[L] != L:
            right[L-1] = right[L]
            ren
        else:
            right[L-1] = L-1

    if R != len(right)-1:
        if right[R] != R:
            right[R+1] = right[R]
        else:
            right[R+1] = R+1

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

    for _ in range(Q):
        q, L, R = map(int, input().split())
        if q == 1:
            rev(left, right, L-1, R-1)
        if q == 2:
            if
main()
