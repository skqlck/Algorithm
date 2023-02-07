T = int(input())
for test_case in range(1,1+T):
    P,A,B = map(int,input().split())
    l_A, r_A = 1, P
    l_B, r_B = 1, P
    c_A, c_B = int((l_A+r_A)/2), int((l_B+r_B)/2)
    while c_A != A and c_B != B:
        if c_A < A:
            l_A = c_A
            c_A = int((l_A+r_A)/2)
        else:
            r_A = c_A
            c_A = int((l_A+r_A)/2)

        if c_B < B:
            l_B = c_B
            c_B = int((l_B+r_B)/2)
        else:
            r_B = c_B
            c_B = int((l_B+r_B)/2)

    if c_A == A and c_B == B:
        print(f"#{test_case} 0")
    elif c_A == A:
        print(f"#{test_case} A")
    else:
        print(f"#{test_case} B")