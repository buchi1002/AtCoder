S = input()

n = sum(1 for s in S if ord("a")<= ord(s) <= ord("z"))

if n <= len(S)//2:
    print(S.upper())
else:
    print(S.lower())