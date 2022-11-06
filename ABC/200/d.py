from collections import deque

def main():
    N = int(input())
    As = list(map(int, input().split()))

    dp = [[0]*200 for _ in range(N)]
    dp[0][0] = 1
    dp[0][As[0]%200] = 1
    for i in range(1,N):
        for j in range(200):
            dp[i][j] += dp[i-1][j] + dp[i-1][(j - As[i])%200]

    s_idx = -1
    for j in range(200):
        if dp[N-1][j] >= 2:
            s_idx = j

    Zflag = False
    if s_idx == 0:
        if dp[N-1][0] == 2:
            s_idx = -1
        else:
            Zflag = True


    if s_idx == -1:
        print("No")
    else:
        print("Yes")

        B = deque()
        C = deque()
        b = c = s_idx
        flag = True
        for i in range(N-1, 0, -1):
            if flag:
                if dp[i-1][(b - As[i])%200] != 0:
                    B.appendleft(i+1)
                    b = (b - As[i])%200

                if (Zflag and dp[i-1][c] >= 2) or ((not Zflag) and dp[i-1][c] >= 1):
                    if dp[i-1][(b - As[i])%200] != 0:
                        flag = False
                else:
                    C.appendleft(i+1)
                    c = (c - As[i])%200
                    Zflag = False
            else:
                if dp[i-1][(b - As[i])%200] != 0:
                    B.appendleft(i+1)
                    b = (b - As[i])%200
                if dp[i-1][(c-As[i])%200] != 0:
                    C.appendleft(i+1)
                    c = (c - As[i])%200

        if b == As[0]%200:
            B.appendleft(1)
        if c == As[0]%200:
            C.appendleft(1)

        B.appendleft(len(B))
        C.appendleft(len(C))
        print(*B)
        print(*C)

    print(dp)
main()
