import math

def main():
    N, X = map(int,input().split())
    dp = [math.inf]*N
    cost = 0
    for i in range(N):
        if X - i <= 0:
            break
        a, b = map(int,input().split())
        dp[i] = cost + a + b*(X-i)
        cost += a + b

    print(min(dp))
if __name__ == '__main__':
    main()
