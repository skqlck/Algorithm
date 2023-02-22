T = int(input())
for test_case in range(1,1+T):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    answer = 0
    answer_start = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                local_start = graph[i][j]
                cnt = 1
                x,y = i,j
                while True:
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<N and 0<=ny<N and graph[x][y] + 1 == graph[nx][ny]:
                            visited[x][y] = 1
                            x,y = nx,ny
                            cnt += 1
                            break
                    else:
                        visited[x][y] = 0
                        break
                if answer < cnt:
                    answer = cnt
                    answer_start = local_start
                elif answer == cnt:
                    answer_start = min(local_start,answer_start)
    print(f"#{test_case} {answer_start} {answer}")