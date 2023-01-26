'''
입력으로 주어진 DFS 탐색 결과(= answer)의 i번째 노드를 u라고 할 때,
u의 subtree size를 S(u)라고 하자.
그렇다면 answer의 i번째 이후로 S(u)개는 전부 u의 서브트리 노드들이어야한다.
또한 answer[i+S(u)] 이후 나오는 노드(= v)는 최소한 u보다 depth가 작거나 같아야한다.
즉, u의 서브트리를 DFS로 순회했다면, 이후 백트래킹은 최소한 u와 형제노드이지,
u의 형제노드의 자식노드라면 u의 형제노드가 빠진것이다.
'''
# import sys
# input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
answer = list(map(int,input().split()))
depths = [0]*(N+1)
visited = [0]*(N+1)
visited[0] = 1
subtree_size = [0]*(N+1)

def dfs(u,depth):
    size = 1
    depths[u] = depth
    for v in tree[u]:
        if not visited[v]:
            visited[v] = 1
            size += dfs(v,depth+1)
    subtree_size[u] = size
    return size
if answer[0] != 1:
    print(0)
else:
    visited[1] = 1
    dfs(1,0)
    for i in range(1,N):
        u = answer[i]
        if subtree_size[u] == 1 or i+subtree_size[u] >= N:
            continue
        v = answer[i+subtree_size[u]]
        if depths[u] < depths[v]:
            print(0)
            break
    else:
        print(1)