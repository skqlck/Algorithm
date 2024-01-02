import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

N,Q = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

for _ in range(Q):
    criteria, start = map(int,input().split())

    visited = [False for _ in range(N+1)]
    visited[start] = True
    queue = deque()
    queue.append((start,1000000001))

    recommendation_cnt = 0

    while queue:
        now, minUsado = queue.popleft()

        for next, nextUsado in graph[now]:
            
            if not visited[next] and nextUsado >= criteria:
                recommendation_cnt+=1
                queue.append((next, nextUsado))
                visited[next] = True

    print(recommendation_cnt)