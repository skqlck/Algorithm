import sys
sys.stdin = open('input.txt')

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x,y):
    parent[find(y)] = find(x)

T = int(input())
for test_case in range(1,1+T):
    V,E = map(int,input().split())
    V += 1
    edges = []
    parent = [i for i in range(V)]
    for _ in range(E):
        edges.append(list(map(int,input().split())))
    edges.sort(key = lambda x : x[2])
    answer = 0
    cnt = 0
    for edge in edges:
        u,v,w = edge
        if find(u) == find(v):
            continue
        union(u,v)
        answer += w
        cnt += 1
        if cnt == V-1:
            break
    print(f"#{test_case} {answer}")
