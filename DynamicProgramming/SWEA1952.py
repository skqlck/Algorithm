T = int(input())
for test_case in range(1,1+T):
    prices = list(map(int,input().split()))
    # 0 1일권, 1 1개월권, 2 3개월권, 3 1년권
    days = [0] + list(map(int,input().split()))
    # days[1] = 1월달 이용할 날
    DP = [[3000,3000,3000] for _ in range(13)]
    DP[12] = [days[12]*prices[0], prices[1], 3000]
    DP[11][0] = min(DP[12][0],DP[12][1]) + days[11]*prices[0]
    DP[11][1] = min(DP[12][0],DP[12][1]) + prices[1]
    DP[11][2] = 3000
    DP[10][0] = min(DP[11][0],DP[11][1]) + days[10]*prices[0]
    DP[10][1] = min(DP[11][0],DP[11][1]) + prices[1]
    DP[10][2] = prices[2]
    for month in range(9,0,-1):
        DP[month][0] = min(DP[month+1]) + days[month]*prices[0]
        DP[month][1] = min(DP[month+1]) + prices[1]
        DP[month][2] = min(DP[month+3]) + prices[2]
    answer = min(DP[1]+[prices[3]])
    print(f"#{test_case} {answer}")