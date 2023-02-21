from collections import deque
def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y,0))
    while queue:
        x,y,step = queue.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nx, ny = x + dx, y + dy
            if (0 > nx or nx >= N) or (0 > ny or ny >= N):
                continue
            if visited[nx][ny]:
                continue
            if maze[nx][ny] == 3:
                print(f"#{test_case} {step}")
                return
            elif maze[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny,step+1))
    else:
        print(f"#{test_case} 0")

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    start_x,start_y = 0,0
    flag = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x,start_y = i,j
                flag = True
                break
        if flag:
            break
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[start_x][start_y] = 1
    visited[start_x][start_y] = 1
    bfs(start_x,start_y)