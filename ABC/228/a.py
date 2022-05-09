def main():
    S, T, X = map(int, input().split())
    if S<T:
        if S<=X and  X<T:
            print("Yes")
        else:
            print("No")
    else:
        if T<=X and X<S:
            print("No")
        else:
            print("Yes")
if __name__ == '__main__':
    main()
