import sys
sys.stdin = open("sample_input.txt","r")
from collections import deque

dx,dy = [1, -1, 0, 0], [0, 0, 1, -1]
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    graph = [[-1 for _ in range(M)] for _ in range(N)]
    queue = deque()
    for i in range(N):
        line = input()
        for j in range(M):
            if line[j] == "W":
                graph[i][j] = 0
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == -1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                answer += graph[i][j]
    print(f"#{test_case} {answer}")