import re

S = input()
patern = '[A-Z][1-9][0-9]{5}[A-Z]'

if re.fullmatch(patern, S):
    print("Yes")
else:
    print("No")
