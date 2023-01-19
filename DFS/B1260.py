'''
1.엣지 개수가 최대 10000개까지 나오므로 sys.stdin.readline 사용
2.인덱스로 노드에 접근하는 것보다 노드 자체로 그래프를 만들어서
  해당 노드의 연결노드를 정렬시켜 탐색하는 것이 빠르다.
  인덱스로 만든다면 연결되지 않는 노드도 탐색해야한다.
'''
from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i] = sorted(graph[i])

def dfs(u):
    print(u, end = ' ')
    for v in graph[u]:
        if not visited[v]:
            visited[v] = 1
            dfs(v)

def bfs(u):
    queue = deque()
    queue.append(u)
    while queue:
        u = queue.popleft()
        print(u, end = ' ')
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
visited[V] = 1
dfs(V)
print()
visited = [0]*(N+1)
visited[V] = 1
bfs(V)