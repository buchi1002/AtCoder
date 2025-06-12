from itertools import product
N = int(input())
d = {"W":"L", "L":"W", "D":"D", "-":"-"}

As = [input() for _ in range(N)]
if all(As[i][j] == d[As[j][i]] for i, j in product(range(N), range(N))):
    print("correct")
else:
    print("incorrect")