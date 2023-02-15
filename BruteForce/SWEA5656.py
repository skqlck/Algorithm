"""
N번 반복
  1.W중에서 하나 선택 후 터트리기
    1-1.연쇄반응 (BFS)
  2.그래프 정리
개수 세기

그래프는 복사해서 사용 (N번)
"""
import sys
sys.stdin = open("sample_input.txt","r")

from collections import deque
def countBlock(graph): # 블록 세기
    cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j]:
                cnt += 1
    return cnt
def BFS(x,y,graph):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            for m in range(1,graph[x][y]):
                nx,ny = x+dx[i]*m, y+dy[i]*m
                if 0<=nx<H and 0<=ny<W and graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
        graph[x][y] = 0

    gravitied = []
    for line in zip(*graph):
        nonzeros, zeros = [],[]
        for element in line:
            if element:
                nonzeros.append(element)
            else:
                zeros.append(element)
        gravitied.append(zeros+nonzeros)
    return list(map(list,zip(*gravitied)))

def DFS(graph, depth):
    global answer
    if answer:
        if depth == N:
            answer = min(answer,countBlock(graph))
            return
        flag = True
        for j in range(W):
            for i in range(H):
                if graph[i][j]:
                    new_graph = [graph[i][:] for i in range(H)]
                    new_graph = BFS(i, j, new_graph)
                    DFS(new_graph,depth+1)
                    flag = False
                    break
        if flag:
            answer = 0


T = int(input())
for test_case in range(1,1+T):
    N,W,H = map(int,input().split())
    origin_graph = [list(map(int,input().split())) for _ in range(H)]
    answer = H*W
    graph = [origin_graph[i][:] for i in range(H)]
    DFS(graph,0)
    print(f"#{test_case} {answer}")