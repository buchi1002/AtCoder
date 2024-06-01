def main():
    N = int(input())
    ans = 1
    for i in range(N+1):
        if i**3 > N:
            break
        K = i**3

        if K == int(str(K)[::-1]):
            ans = K

    print(ans)
main()
