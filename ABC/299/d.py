def main():
    N = int(input())
    s_idx = 0
    s_v = 0
    e_v = 1
    e_idx = N-1
    while s_idx + 1 != e_idx:
        m_idx = (s_idx+e_idx)//2
        print("? " + str(m_idx+1))
        m_v = int(input())

        if m_v != s_v:
            e_idx = m_idx
            e_v = m_v
        else:
            s_idx = m_idx
            s_v = m_v

    print("! " + str(e_idx))

main()
