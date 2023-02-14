"""
0출발 99도착
단방향 엣지
"""
import sys
sys.stdin = open("input.txt","r")
def dfs(start):
    global exist
    if exist:
        return
    if start == 99:
        exist = True
        return
    for node in graph[start]:
        if not visited[node]:
            visited[node] = 1
            dfs(node)
    return

for test_case in range(1,11):
    E = int(input().split()[1])

    graph = [[] for _ in range(100)]
    visited = [0]*100

    edges = list(map(int,input().split()))
    for i in range(0,E):
        graph[edges[2*i]].append(edges[2*i+1])

    exist = False
    dfs(0)
    if exist:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")