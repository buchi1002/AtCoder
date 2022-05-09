######################
#自作
def Q(A, p, r, dic):
    if p<r:
        q = P(A, p,r, dic)
        Q(A, p, q-1, dic)
        Q(A, q+1, r, dic)

def P(A, p, r, dic):
    x = A[r]
    i = p-1
    for j in range(p, r):
        L = min(len(A[j]), len(x))
        l = 0
        d = 0
        while l < L:
            if dic[A[j][l]] < dic[x[l]]:
                i = i+1
                A[i], A[j] = A[j], A[i]
                break
            elif dic[A[j][l]] > dic[x[l]]:
                break
            elif l == L-1 and len(A[j]) < len(x):
                i = i+1
                A[i], A[j] = A[j], A[i]
            l += 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def main():
    X = input()
    N = int(input())

    dic = {}
    for i in range(len(X)):
        dic[X[i]] = i

    Ss = [""]*N

    for i in range(N):
        Ss[i] = input()

    Q(Ss, 0, len(Ss)-1, dic)

    for i in range(N):
        print(Ss[i])


if __name__ == '__main__':
    main()

###########################################################
#### cmt_to_key


from functools import cmp_to_key

X = input()
N = int(input())
Ss = [""]*N

for i in range(N):
    Ss[i] = input()
L = len(X)
dic = {}
for i in range(L):
    dic[X[i]] = i

def cmp(a, b):
    l = min(len(a), len(b))
    for i in range(l):
        if dic[a[i]] < dic[b[i]]:
            return -1
        if dic[a[i]] > dic[b[i]]:
            return 1
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    return 0

def main():
    S = sorted(Ss, key=cmp_to_key(cmp))

    for i in S:
        print(i)

if __name__ == '__main__':
    main()
