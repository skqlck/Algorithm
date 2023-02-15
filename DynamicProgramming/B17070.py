N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
DP = [[[0,0,0] for _ in range(N)] for _ in range(N)]
for j in range(1,N):
    if graph[0][j] == 1:
        break
    DP[0][j] = [1,0,0]

for i in range(1,N):
    for j in range(2,N):
        if graph[i][j]:
            continue
        DP[i][j][0] = DP[i][j-1][0]+DP[i][j-1][2]
        DP[i][j][1] = DP[i-1][j][1]+DP[i-1][j][2]
        for dx,dy in [[-1,-1],[0,-1],[-1,0]]:
            if graph[i+dx][j+dy] == 1:
                break
        else:
            DP[i][j][2] = sum(DP[i-1][j-1])
print(sum(DP[N-1][N-1]))