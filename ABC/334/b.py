def main():
    A, M, L, R = map(int, input().split())
    R = R - A + (10**20)*M
    L = L - A + (10**20)*M

    l = L//M - (L%M==0)
    r = R//M

    print(r-l)

main()
