def main():
    N = int(input())
    L = [1]*(2*10**5+1)
    L[1] = L[0] = 0
    L[2]=1
    for i in range(2,len(L)):
        if L[i] == 1:
            k = 2
            while i*k<=2*10**5:
                L[i*k] = 0
                k += 1
    print(L.count(1))
if __name__ == '__main__':
    main()
