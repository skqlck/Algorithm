N = int(input())
graph = [[] for _ in range(N)]
E = int(input())
for edge in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

"""
다 때려박고 하는 방법
"""
visited = [0]*N
visited[0] = 1
stack = [0]
while stack:
    out = stack.pop()
    print(out)
    for node in graph[out]:
        if not visited[node]:
            stack.append(node)
            visited[node] = 1

"""
하나씩 하는 방법
"""
stack = [0]
visited = [0]*N
visited[0] = 1
print(0)
answer = []
while stack:
    for node in graph[stack[-1]]:
        if not visited[node]:
            stack.append(node)
            visited[node] = 1
            break
    else:
        answer.append(stack.pop())
print(*answer[::-1])

"""
              0
        1           2
    3       4   5       6
"""