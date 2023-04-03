import sys
sys.stdin = open('input.txt')

from collections import deque
D = ((1,0),(0,1),(-1,0),(0,-1))
T= int(input())
for test_case in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[1000000 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] > visited[x][y]+1+max(0,graph[nx][ny]-graph[x][y]):
                    visited[nx][ny] = visited[x][y]+1+max(0,graph[nx][ny]-graph[x][y])
                    queue.append((nx,ny))

    print(f"#{test_case} {visited[N-1][N-1]}")