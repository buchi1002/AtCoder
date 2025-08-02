S = input()
T = set(s for s in input())

if all(S[i-1] in T for i in range(1, len(S)) if S[i] == S[i].upper()):
    print("Yes")
else:
    print("No")