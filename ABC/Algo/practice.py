def step2():
    N = 4
    As = [10, 2, 5, 1]

    L = 2**N
    max_kinomi = 0
    for i in range(L):
        kinomi = 0
        number_of_tree = 0

        s =  bin(i)[2:]
        s_len = len(s)
        s = "0"*(N-s_len) + s
        for j in range(N):
            if s[j] == "1":
                number_of_tree += As[j]
            else:
                kinomi += number_of_tree

        if max_kinomi < kinomi:
            max_kinomi = kinomi

        print(max_kinomi)

step2()
