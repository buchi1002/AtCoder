T = int(input())

for _ in range(T):
    N = int(input())
    Ss = list(map(int, input().split()))
    Ts = sorted(Ss[1:N-1]) + [Ss[-1]]
    ans = [Ss[0]]
    i = 0
    while i < len(Ts):
        if ans[-1] * 2 >= Ss[-1]:
            ans.append(Ss[-1])
            break
        if ans[-1] * 2 >= Ts[i]:
            if i < len(Ts) - 1:
                if ans[-1] * 2 >= Ts[i + 1]:
                    i += 1
                else:
                    ans.append(Ts[i])
                    i += 1
            else:
                ans.append(Ts[i])
                break
        else:
            break

    if ans[-1] != Ss[-1]:
        print(-1)
    else:
        print(len(ans))