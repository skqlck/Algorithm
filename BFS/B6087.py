# import sys
# input = sys.stdin.readline
from collections import deque
def balsa(start_x,start_y):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    queue.append((start_x,start_y,-1))
    while queue:
        x,y,mirror = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            while 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == '.':
                        visited[nx][ny] = 1
                        queue.append((nx,ny,mirror+1))
                        nx += dx[i]
                        ny += dy[i]
                elif not visited[nx][ny] and graph[nx][ny] == 'C':
                        print(mirror+1)
                        return
                else:
                    break

M,N = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == "C":
            x, y = i, j
            flag = True
            break
    if flag:
        break
visited[x][y] = 1
balsa(x,y)


