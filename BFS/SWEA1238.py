import sys
sys.stdin = open("input.txt","r")

from collections import deque
for test_case in range(1,11):
    N,start = map(int,input().split())
    graph = [[0 for _ in range(101)] for _ in range(101)]
    Edges = list(map(int,input().split()))
    visited = [0]*101
    for i in range(0,N,2):
        u,v = Edges[i],Edges[i+1]
        graph[u][v] = 1
    queue = deque()
    queue.append(start)
    while queue:
        receivers = []
        for _ in range(len(queue)):
            caller = queue.popleft()
            receivers.append(caller)
            for receiver in range(1,101):
                if graph[caller][receiver] and not visited[receiver]:
                    queue.append(receiver)
                    visited[receiver] = 1
    print(f"#{test_case} {max(receivers)}")