import math

S = set([0])
dic = dict()
dic[0] = 1

def function(k):
    if k in S:
        return dic[k]
    else:
        r = function(k//2) + function(k//3)
        S.add(k)
        dic[k] = r
        return r

N = int(input())

print(function(N))
