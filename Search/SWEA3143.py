import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    A,B = input().split()
    N,M = len(A),len(B)
    idx = 0
    cnt = 0
    while idx < N:
        cnt += 1
        if idx + M - 1 < N and A[idx:idx+M] == B:
            idx += M
            continue
        idx += 1
    print(f"#{test_case} {cnt}")