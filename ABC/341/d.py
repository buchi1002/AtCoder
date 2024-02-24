from math import gcd
#二分探索の基本コード
def binary_search(lcm_NM, N, M, R):
    l=0
    r=lcm_NM-1
    while r-l+1>=1:
        m=(l+r)//2
        v = m//N + m//M
        if v == R:
            if m%N==0 or m%M==0:
                return m
            else:
                r = m-1
        elif v < R:
            l = m + 1
        elif v > R:
            r = m - 1
    return -1

def main():
    N, M, K = map(int, input().split())
    N, M = max(N, M), min(N, M)
    lcm_NM = (N*M)//gcd(N, M)
    cnt = (lcm_NM//N) + (lcm_NM//M) - 2
    ans = ((K//cnt) - ((K%cnt)==0))*lcm_NM
    R = K - ((K//cnt) - ((K%cnt)==0))*cnt
    ans += binary_search(lcm_NM, N, M, R)
    print(ans)


main()
