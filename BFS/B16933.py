'''
주석대로...
방문처리는 해당 좌표를 방문하는데 벽을 부순 개수를 표시하는데,
이는 더 오래 걸리더라도 벽을 덜 부수고 왔다면, 나중에 벽을 부수는 데
사용할 수 있다. 즉, 최단거리로 왔지만 벽을 더 이상 부술 수 없어 더 이상
진행이 불가능한 경우를 대비해, 벽을 덜 부수고 온 것들은 큐에 집어넣어준다.
'''
from collections import deque
#import sys
#input = sys.stdin.readline

N,M,K = map(int,input().split())

graph = [list(input()) for _ in range(N)]

visited = [[N*M for _ in range(M)] for _ in range(N)]

def bfs():
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    ## queue에는 x,y,cnt,밤0낮1,wall
    queue.append([0,0,1,1,0])
    while queue:
        x,y,cnt,day,wall = queue.popleft()
        if x == N-1 and y == M-1:
            return cnt
        # 상하좌우로 움직이는 경우
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                ## 빈공간을 만났을때
                if graph[nx][ny] == '0':
                    if visited[nx][ny] > wall:
                        visited[nx][ny] = wall
                        queue.append([nx,ny,cnt+1,(day+1)%2,wall])
                ## 벽을 만났을 때            
                else:
                    # 벽을 부수는 게 맞고 벽을 부술 수 있다면...
                    if visited[nx][ny] > (wall + 1) and wall < K: 
                        if day: #낮이고
                            visited[nx][ny] = wall + 1
                            queue.append([nx,ny,cnt+1,0,wall+1])
                        else: #밤이라면 하루를 뛴다고 생각
                            visited[nx][ny] = wall +1
                            queue.append([nx,ny,cnt+2,0,wall+1])
    return -1

print(bfs())