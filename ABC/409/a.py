def main():
    N = int(input())
    T = input()
    A = input()
    if any(T[i] == A[i] == "o" for i in range(N)):
        print("Yes")
    else:
        print("No")

main()