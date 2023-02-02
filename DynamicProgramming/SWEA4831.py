"""
메모제이션을 통해 DP[i] = i지점까지 도착하는데 최소 충전횟수
"""
T = int(input())
for test_case in range(1,1+T):
    K,N,M = map(int,input().split())
    DP = [-1 for _ in range(N+1)]
    station = list(map(int,input().split()))
    DP[0] = 0
    flag = False
    for k in range(0,K+1):
        DP[k] = 0
    for s in station:
        if DP[s] == -1:
            print(f"#{test_case} 0")
            flag = True
            break
        for k in range(1,K+1):
            if s+k < N+1:
                if DP[s+k] == -1:
                    DP[s+k] = DP[s]+1
                else:
                    DP[s+k] = min(DP[s]+1,DP[s+k])
    if flag:
        continue
    else:
        print(f"#{test_case} {DP[N]}")