import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,1+T):
    arr = list(map(int,input().split()))
    N = arr[0]
    arr = arr[1:]+[0]
    DP = [N]*N
    for i in range(arr[0]+1):
        DP[i] = 0
    for i in range(N-1):
        for j in range(1,arr[i]+1):
            if i+j < N:
                DP[i+j] = min(DP[i+j],DP[i]+1)
    print(f"#{test_case} {DP[N-1]}")