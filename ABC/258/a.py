def main():
    K = int(input())
    h = K//60
    m = K%60

    print(str(21+h).zfill(2) + ":" + str(m).zfill(2))
if __name__ == '__main__':
    main()
