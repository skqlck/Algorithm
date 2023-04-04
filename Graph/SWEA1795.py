import sys
sys.stdin = open('input.txt')

def back_dijkstra(start): # go to 생일 파티
    U = [0]*N
    U[start] = 1
    D = [0]*N
    for i in range(N):
        D[i] = graph[start][i]
    for _ in range(N-1):
        minV = 1010000
        w = -1
        for i in range(N):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(N):
            if 0 < graph[w][v] < INF:
                D[v] = min(D[v], D[w]+graph[w][v])
    return D

def go_dijkstra(start): # come back home
    U = [0]*N
    U[start] = 1
    D = [0]*N
    for i in range(N):
        D[i] = graph[i][start]

    for _ in range(N-1):
        minV = 1010000
        w = -1
        for i in range(N):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(N):
            if 0 < graph[v][w] < INF:
                D[v] = min(D[v], D[w]+graph[v][w])
    return D

T = int(input())
INF = 101
for test_case in range(1,1+T):
    N,M,X = map(int,input().split())
    X -= 1
    graph = [[INF*N for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    for _ in range(M):
        u,v,w = map(int,input().split())
        graph[u-1][v-1] = w
    go_D = go_dijkstra(X)
    back_D = back_dijkstra(X)
    answer = 0
    for i in range(N):
        if answer < go_D[i] + back_D[i]:
            answer = go_D[i] + back_D[i]
    print(f"#{test_case} {answer}")