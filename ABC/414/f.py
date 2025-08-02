def main():
    N, K = map(int, input().split())
    As = tuple(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= As[i]
        if ans >= 10 ** K:
            ans = 1
    
    print(ans)
main()