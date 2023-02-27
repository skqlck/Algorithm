import sys
sys.stdin = open("sample_input.txt","r")

from collections import deque
def bfs(start_x,start_y):
    global answer
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    visited = set()
    queue = deque()
    queue.append((start_x,start_y,1,1,graph[start_x][start_y]))
                # 시작 row, 시작 col, step, cheat, 현재 높이
    visited.add((start_x,start_y,1))
    while queue:
        x,y,step,cheat,now = queue.popleft()
        answer = max(answer,step)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and (nx,ny) not in visited:
                if graph[nx][ny] < now:
                    queue.append((nx,ny,step+1,cheat,graph[nx][ny]))
                    visited.add((nx,ny,step+1))
                else:
                    if cheat and graph[nx][ny]-K < now:
                        visited.add((nx,ny,step+1))
                        queue.append((nx,ny,step+1,0,now - 1))

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
    for x,y in Bongs:
        bfs(x,y)
    print(f"#{test_case} {answer}")
