A, B, C, D, E, F, X = map(int, input().split())
t = (X//(A + C))*(A*B) + min(X%(A + C), A)*B
a = (X//(D + F))*(D*E) + min(X%(D + F), D)*E

if a < t:
    print("Takahashi")
elif a > t:
    print("Aoki")
else:
    print("Draw")