for i in range(8):
    S = input()
    for j in range(8):
        if S[j] == "*":
            print(chr(97+j)+str(8-i))
