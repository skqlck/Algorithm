# import sys
# sys.stdin = open("input.txt","r")
""""""
from collections import deque

def balsa(x,y):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    # 초기화
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        while 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == '.':
                visited[nx][ny] = 0
                queue.append((nx,ny))
            elif (nx,ny) == end:
                print(0)
                return
            else:
                break
            nx += dx[i]
            ny += dy[i]

    while queue:
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                while 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny] == '.':
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx,ny))
                        elif visited[nx][ny] == visited[x][y] + 1:
                            pass
                        else:
                            break
                    elif (nx,ny) == end:
                        print(visited[x][y]+1)
                        return
                    else:
                        break
                    nx += dx[i]
                    ny += dy[i]

M,N = map(int,input().split())
graph = []
start,end = tuple(),tuple()
for i in range(N):
    line = list(input().rstrip())
    graph.append(line)
    for j in range(M):
        if line[j] == "C":
            if start:
                end = (i,j)
                break
            start = (i,j)
visited = [[-1 for _ in range(M)] for _ in range(N)]
x,y = start
visited[x][y] = 0
balsa(x,y)
