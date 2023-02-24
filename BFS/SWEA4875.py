import sys
sys.stdin = open("../BruteForce/sample_input.txt", "r")

from collections import deque
def bfs():
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    queue.append(start)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if maze[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] =1
                elif maze[nx][ny] == 3:
                    return 1
    return 0

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input().strip())) for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i,j)
                flag = True
                break
        if flag:
            break


    visited = [[0 for _ in range(N)] for _ in range(N)]

    print(f"#{test_case} {bfs()}")