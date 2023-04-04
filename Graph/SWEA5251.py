import sys
sys.stdin = open('input.txt')

def dijkstra(start):
    U = [0]*V
    for i in range(V):
        D[i] = graph[start][i]

    for _ in range(V):
        minV = INF
        w = 0
        for i in range(V):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                w = i

        U[w] = 1
        for v in range(V):
            if 0 < graph[w][v] < INF:
                D[v] = min(D[v], D[w]+graph[w][v])

T = int(input())
INF = 10000
for test_case in range(1,1+T):
    V,E = map(int,input().split())
    V += 1
    graph = [[INF for _ in range(V)] for _ in range(V)]
    for i in range(V):
        graph[i][i] = 0
    for _ in range(E):
        u,v,w = map(int,input().split())
        graph[u][v] = w
    D = [0] * V
    dijkstra(0)
    print(f"#{test_case} {D[V-1]}")