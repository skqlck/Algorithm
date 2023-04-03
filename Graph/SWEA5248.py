import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N)]
    love_arrows = list(map(int,input().split()))
    visited= [0]*N
    for i in range(M):
        u,v = love_arrows[2*i]-1,love_arrows[2*i+1]-1
        graph[u].append(v)
        graph[v].append(u)
    answer = 0
    queue = deque()
    for u in range(N):
        if not visited[u]:
            answer += 1
            queue.append(u)
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = 1
                        queue.append(v)

    print(f"#{test_case} {answer}")