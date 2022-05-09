def main():
    A, B = list(map(int, input().split()))
    if B <= 6*A and A <= B:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
