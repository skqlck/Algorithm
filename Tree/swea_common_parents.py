from collections import deque

def common_parents(u,v):
    path_u, path_v = [],[]
    while u != 0 or v != 0:
        if u != 0:
            path_u.append(u)
            u = parents[u]
        if v != 0:
            path_v.append(v)
            v = parents[v]
    n = min(len(path_u),len(path_v))
    parent = 0
    for i in range(-1,-n,-1):
        if path_u[i] != path_v[i]:
            return parent
        parent = path_u[i]
    return parent

def subtree_size(root):
    cnt = 1
    queue = deque()
    queue.append(root)
    while queue:
        u = queue.popleft()
        cnt += len(children[u])
        queue.extend(children[u])
    return cnt

T = int(input())
for test_case in range(1,1+T):
    V,E,node1,node2 = map(int,input().split())
    parents = [0 for _ in range(V)]
    children = [[] for _ in range(V)]
    edges = list(map(int,input().split()))
    for i in range(0,2*E,2):
        parent,child = edges[i]-1,edges[i+1]-1
        parents[child] = parent
        children[parent].append(child)
    parent = common_parents(node1-1,node2-1)
    size = subtree_size(parent)
    print(f"#{test_case} {parent+1} {size}")