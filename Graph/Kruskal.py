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
def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)


V,E = map(int,input().split())
rep = [i for i in range(V+1)]
Edges = []
for _ in range(E):
    u,v,w = map(int,input().split())
    Edges.append([u,v,w])

Edges.sort(key = lambda x : x[2])

N = V + 1 # 노드 개수
s = 0 # MST에 포함된 엣지의 가중치 합
cnt = 0 # 선택한 엣지 개수
for edge in Edges:
    u,v,w = edge
    if find_set(u) == find_set(v):
        continue
    union(u,v)
    cnt += 1
    s += w
    if cnt == N-1:
        break
print(s)
