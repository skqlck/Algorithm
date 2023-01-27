# import sys
# input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
'''
싸이클 찾기
* 현재 노드에서 DFS를 하여 현재 노드가 나온다면 DFS한 순서대로 싸이클을 이룬다.
* 싸이클을 원소의 최소 개수는 3
'''
def get_cycle(u,path):
    global flag
    global cycle
    if flag:
        return
    for v in graph[u]:
        if not visited[v]:
            visited[v] = 1
            path.append(v)
            get_cycle(v,path)
            visited[v] = 0
            path.pop()
        elif len(path) >= 3 and v == path[0]:
            cycle = path[:]
            flag = 1
            return
flag = 0
cycle = []
for u in range(1,N+1):
    visited[u] = 1
    get_cycle(u,[u])

distance = [-1]*(N+1)
for c in cycle:
    distance[c] = 0
visited = [0]*(N+1)
visited[cycle[0]] = 1
def bfs():
    queue = deque()
    queue.append(cycle[0])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = 1
                if distance[v] == 0:
                    queue.append(v)
                elif distance[v] == -1:
                    distance[v] = distance[u]+1
                    queue.append(v)
bfs()
print(' '.join(map(str,(distance[1:]))))