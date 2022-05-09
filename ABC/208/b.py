import math
def main():
    p = int(input())

    count = 0
    i = 0
    MS = [10, 9, 8, 7, 6, 5, 4, 3, 2 ,1]
    while p != 0 or i >= 10:
        m = math.factorial(MS[i])
        if p - m >=0:
            p -= m
            count += 1
        else:
            i += 1
    print(count)
if __name__ == '__main__':
    main()
