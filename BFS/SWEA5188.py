from collections import deque
T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    queue = deque()
    visited = [[10*N*N for _ in range(N)] for  _ in range(N)]
    visited[0][0] = graph[0][0]
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue.append([0,0])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]+visited[x][y] < visited[nx][ny]:
                    visited[nx][ny] = graph[nx][ny]+visited[x][y]
                    queue.append([nx,ny])
    print(f"#{test_case} {visited[N-1][N-1]}")

