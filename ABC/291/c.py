N = int(input())
S = input()

Set = set()
x = 0
y = 0
Set.add((y, x))
for i in range(len(S)):
    s = S[i]
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    elif s == "D":
         y -= 1

    Set.add((y, x))

if len(Set) != (N+1):
    print("Yes")
else:
    print("No")
