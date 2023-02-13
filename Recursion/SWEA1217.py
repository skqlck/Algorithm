def power(N,M):
    if M == 1:
        return N
    return N*power(N,M-1)

for test_case in range(1,11):
    input()
    N,M = map(int,input().split())
    print(f"#{test_case} {power(N,M)}")