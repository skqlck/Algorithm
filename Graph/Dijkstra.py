"""
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""

def dijkstra(s,V):
    # U 최소 비용이 결정된 정점 집합 (visited 형식으로 만들기)
    U = [0] * (V+1)
    U[s]= 1
    for i in range(V+1):
        D[i] = graph[s][i]
    # N개의 정점
    N = V+1
    # 남은 정점의 비용 결정
    for _ in range(N-1): # N-1개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        # w에 인접인 정점에 대해, 기존 비용 vs w를 거쳐가는 비용
        for v in range(V+1):
            if 0 < graph[w][v] < INF: # w에 인접인 v의 조건
                D[v] = min(D[v], D[w]+graph[w][v])

INF = 1000 # 노드 수 x 최대 가중치정도로
V, E = map(int,input().split())
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]
for i in range(V+1):
    graph[i][i] = 0

for _ in range(E):
    u,v,w = map(int,input().split())
    # 유향 그래프    u -> v 가중치 w
    graph[u][v] = v

D = [0]*(V+1)

dijkstra(0,V)
print(D)