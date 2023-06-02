X, Y, Z = map(int,input().split())
S = input()

G = [[0]*len(S) for _ in range(2)]
if S[0] == "a":
    G[0][0] = X
    G[1][0] = Z+Y
else:
    G[0][0] = Y
    G[1][0] = Z+X

for i in range(1, len(S)):
    if S[i] == "a":
        G[0][i] = min(G[0][i-1] + X, G[1][i-1] + Z + X)
        G[1][i] = min(G[0][i-1] + Z + Y, G[1][i-1] + Y)
    else:
        G[0][i] = min(G[0][i-1] + Y, G[1][i-1] + Z + Y)
        G[1][i] = min(G[0][i-1] + Z + X, G[1][i-1] + X)

print(min(G[0][len(S)-1], G[1][len(S)-1]))
