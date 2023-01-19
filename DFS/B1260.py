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