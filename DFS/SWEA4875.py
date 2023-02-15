T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input().strip())) for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i,j]
                flag = True
                break
        if flag:
            break

    visited = [[0 for _ in range(N)] for _ in range(N)]

    stack = [start]
    visited[start[0]][start[1]] = 1
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    answer = 0
    while stack:
        x,y = stack[-1]
        if maze[x][y] == 3:
            answer = 1
            break

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and maze[nx][ny] in (0,3):
                stack.append([nx,ny])
                visited[nx][ny] = 1
                break
        else:
            stack.pop()
    print(f"#{test_case} {answer}")
