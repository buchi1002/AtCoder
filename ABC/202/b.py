def main():
    # input
    S = input()
    # compute
    S = S.replace('6', 'a')
    S = S.replace('9', '6')
    S = S.replace('a', '9')
    S = ''.join(list(reversed(S)))
    # output
    print(S)
if __name__ == '__main__':
    main()
