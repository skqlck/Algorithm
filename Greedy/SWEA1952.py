T = int(input())
for test_case in range(1,1+T):
    prices = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    DP = [[0,0,0] for _ in range(12)]
    DP[0][0] = plan[0]*prices[0]
    DP[0][1] = prices[1]
    DP[0][2] = plan[2]
    for i in range(1,3):
        DP[i][0] = min(DP[i][0], DP[i][1]) + plan[1] * prices[1]
        DP[i][1] = min(DP[i][0], DP[i][1]) + prices[1]
        DP[i][2] = plan[2]
    DP[2][0] = min(DP[1][0],DP[1][1])+plan[2]*prices[1]
    DP[2][1] = min(DP[2][0],DP[2][1])+prices[1]
    DP[2][2] = plan[2]