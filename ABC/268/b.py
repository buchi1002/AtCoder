def main():
    S = input()
    T = input()

    f = T.startswith(S)
    print("Yes"*f + "No"*(1-f))

if __name__ == '__main__':
    main()
