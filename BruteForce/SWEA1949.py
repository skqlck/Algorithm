import sys
sys.stdin = open("sample_input.txt","r")

from collections import deque
# def bfs(start_x,start_y):
#     global answer
#     dx,dy = [1,-1,0,0],[0,0,1,-1]
#     queue = deque()
#     path = [(start_x,start_y)]
#     queue.append((path,1,1,graph[start_x][start_y]))
#                 # 시작 row, 시작 col, step, cheat, 현재 높이
#     while queue:
#         path,step,cheat,now = queue.popleft()
#         x, y = path[-1]
#         answer = max(answer,step)
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if 0<=nx<N and 0<=ny<N and (nx,ny) not in path:
#                 if graph[nx][ny] < now:
#                     temp = path[:]
#                     temp.append((nx,ny))
#                     queue.append((temp,step+1,cheat,graph[nx][ny]))
#                 else:
#                     if cheat and graph[nx][ny]-K < now:
#                         temp = path[:]
#                         temp.append((nx, ny))
#                         queue.append((temp,step+1,0,now-1))

def dfs(x,y,depth,cheat,now):
    global answer
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            if graph[nx][ny] < now:
                visited[nx][ny] = 1
                dfs(nx,ny,depth+1,cheat,graph[nx][ny])
                visited[nx][ny] = 0
            elif cheat and graph[nx][ny] - K < now:
                visited[nx][ny] = 1
                dfs(nx,ny,depth+1,0,now-1)
                visited[nx][ny] = 0
    if answer < depth:
        answer = depth


T = int(input())
for test_case in range(1,1+T):
    N,K = map(int,input().split())
    graph = []
    Bongs = []
    highest = -1
    for i in range(N):
        line = list(map(int,input().split()))
        for j in range(N):
            if line[j] > highest:
                Bongs = []
                Bongs.append((i,j))
                highest = line[j]
            elif line[j] == highest:
                Bongs.append((i,j))
        graph.append(line)
    answer = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x,y in Bongs:
        visited[x][y] = 1
        dfs(x,y,1,1,graph[x][y])
        visited[x][y] = 0
    print(f"#{test_case} {answer}")
