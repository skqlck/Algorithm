from collections import deque
import sys
sys.stdin = open("sample_input.txt","r")

D = [[],
     [(1,0),(-1,0),(0,1),(0,-1)],
     [(1,0),(-1,0)],
     [(0,1),(0,-1)],
     [(-1,0),(0,1)],
     [(1,0),(0,1)],
     [(0,-1),(1,0)],
     [(0,-1),(-1,0)]]
for test_case in range(1,int(input())+1):
    N,M,R,C,L = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((R,C,1))
    visited[R][C] = 1
    answer = 1
    while queue:
        x,y,time = queue.popleft()
        if time == L:
            continue
        for dx,dy in D[graph[x][y]]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                if (-dx,-dy) not in D[graph[nx][ny]]:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    answer += 1
                    queue.append((nx,ny,time+1))
    print(f"#{test_case} {answer}")
