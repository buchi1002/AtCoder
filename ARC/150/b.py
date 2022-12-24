import math

def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int,input().split())

        q = 1
        L = list()
        while q**2 < B + 10:
            L.append(math.ceil(B/q))
            q += 1

        L += list(range(1, math.floor(math.sqrt(B+10))))

        m = math.inf
        for Q in L:
            k = math.ceil(B/Q)
            v = (k+1)*max(0, math.ceil((B/k))-A) + k*A - B

            m = min(v,m)

        print(m)

main()
