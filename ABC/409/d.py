from functools import cmp_to_key

# 比較関数
def compare_items(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = int(input())
        m = 0
        ms = S[0]
        length = 1
        c = 1
        while c + length < N:
            if S[] > S[c + length]:
                m = c

main()