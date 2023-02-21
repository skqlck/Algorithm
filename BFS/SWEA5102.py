from collections import deque
T = int(input())
for test_case in range(1,1+T):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    start,end = map(int,input().split())
    visited = [0]*(V+1)
    visited[start] = 1
    queue = deque()
    queue.append((start,0))
    while queue:
        u,step = queue.popleft()
        if u == end:
            print(f"#{test_case} {step}")
            break
        for v in graph[u]:
            if not visited[v]:
                visited[v] = 1
                queue.append((v,step+1))
    else:
        print(f"#{test_case} 0")
