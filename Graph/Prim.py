"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

def prim():
    U = [0]*V
    D = [1e10] * V
    D[0] = 0
    for _ in range(V-1):
        # D에서 제일 작은 값인 index를 찾는다.
        # U에 없는 v 기준으로
        minV = 1e10
        for i in range(V):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                v = i

        # v를 U에 넣는다.
        U[v] = 1

        # v하고 연결된 w의 D값을 최선으로 수정한다.
        for w in range(V):
            if w in U:
                continue
            if graph[v][w]:
                D[w] = min(D[w], graph[v][w])
    print(D)
    print(U)

V,E = map(int,input().split())
V += 1
graph = [[0 for _ in range(V)] for _ in range(V)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u][v] = w
    graph[v][u] = w

prim()