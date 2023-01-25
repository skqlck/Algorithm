'''
기존 RGB문제와 다르게 처음과 끝이 서로 다른 색이어야한다.
그러므로 첫 집의 색깔(R,G,B)별로 각각 DP를 이용해 최소 비용을 구하고
그 세 개의 최소비용 중 최소값을 출력한다.

* 꼭 세 개를 한번에 구해야할까?
  -> 그렇다. DP[N-1]이 어떠한 DP(색깔들)을 밟고 지나온 지 알 수 없으므로
     세 개를 따로 구해야한다.
'''
N = int(input())
RGB = [0,0,0]
house = []
for i in range(N):
    house.append(list(map(int,input().split())))

## 1 < N < 1001
for i in range(3):
    DP = [[0,0,0] for _ in range(N)]
    DP[0][i] = house[0][i]
    DP[1][i] = 10000
    DP[1][(i+1)%3] = DP[0][i] + house[1][(i+1)%3]
    DP[1][(i+2)%3] = DP[0][i] + house[1][(i+2)%3]
    for j in range(2,N):
        DP[j][0] = min(DP[j-1][1],DP[j-1][2]) + house[j][0]
        DP[j][1] = min(DP[j-1][0],DP[j-1][2]) + house[j][1]
        DP[j][2] = min(DP[j-1][0],DP[j-1][1]) + house[j][2]
    RGB[i] = min(DP[N-1][(i+1)%3],DP[N-1][(i+2)%3])
print(min(RGB))