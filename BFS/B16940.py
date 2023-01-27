'''
BFS 탐색으로 depth별로 노드들을 분류하고
set(해당 depth를 가진 노드) == set(문제의 BFS 단계)
            or 
sorted('') == sorted("") 확인
=> 이렇게 하면 안돼
부모 노드가 먼저 나왔다면, 자식노드도 먼저 나와야한다.
== 사촌 간의 순서가 중요 
부모 빼고 -> 자식 넣고 -> 부모 넣고 -> 자식 넣고 -> ...
'''
# import sys
# input = sys.stdin.readline
from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]
children = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

answer = list(map(int,input().split()))
if answer[0] != 1:
    print(0)
else: 
    visited = [0]*(N+1)

    def bfs():
        queue = deque()
        queue.append(1)
        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                visited[u] = 1
                for v in tree[u]:
                    if not visited[v]:
                        queue.append(v)
                        children[u].append(v)
    bfs()

    # 굳이 함수를?
    start = 1
    queue = deque(answer)
    while queue:
        parent = queue.popleft()
        # set 만드는데 O(n) 비교하는데 O(n)
        if set(answer[start:start+len(children[parent])]) != set(children[parent]):
            print(0)
            break
        start += len(children[parent])
    else:
        print(1)