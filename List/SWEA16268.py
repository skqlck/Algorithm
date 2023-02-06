T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    balloons = [list(map(int,input().split())) for _ in range(N)]
    dx,dy = [1,-1,0,0], [0,0,1,-1]
    answer = 0
    for x in range(N):
        for y in range(M):
            local_sum = balloons[x][y]
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    local_sum += balloons[nx][ny]

            if local_sum > answer:
                answer = local_sum

    print(f"#{test_case} {answer}")

