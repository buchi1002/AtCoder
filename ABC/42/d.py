def combifunc(n,r,L,Lr,p):
    return (((L[n]*Lr[r])%p)*Lr[n-r])%p

def main():
    p = 10**9+7

    H, W, A, B = map(int, input().split())

    L =  [0]*(2*100000+2)
    L[0] = 1
    Lr = [0]*(2*100000+2)
    Lr[0] = 1
    s = 1
    for i in range(1,2*100000+2):
        L[i] = (L[i-1]*i)%p
        Lr[i] = pow(L[i],-1,p)


    dp = [[0]*W for _ in range(2)]

    for j in range(B,W):
        dp[0][j] = combifunc(H-A-1+j,j,L,Lr,p)%p


    for j in range(B,W):
        dp[1][W-1] = (dp[1][W-1] + dp[0][j]*combifunc((A-1)+W-1-j,A-1,L,Lr,p)%p)%p

    print(dp[1][W-1])
if __name__ == '__main__':
    main()
