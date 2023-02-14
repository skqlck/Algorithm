T = int(input())
for test_case in range(1,1+T):
    N = int(input())//10
    DP = [0]*31
    DP[1] = 1
    DP[2] = 3
    for i in range(3,N+1):
        DP[i] = 2*DP[i-2] + DP[i-1]
    print(f"#{test_case} {DP[N]}")