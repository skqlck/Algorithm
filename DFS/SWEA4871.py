import sys
sys.stdin = open("sample_input.txt","r")

def DFS(start):
    global exist
    if start == end:
        exist = True

    for node in graph[start]:
        if not visited[node]:
            visited[node] = 1
            DFS(node)
    return

T = int(input())
for test_case in range(1,1+T):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
    start,end = map(int,input().split())
    visited = [0]*(V+1)
    exist = False
    DFS(start)
    if exist:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")