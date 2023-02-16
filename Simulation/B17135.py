from collections import deque
from itertools import combinations
"""
궁수 3명 (N번째 행에 존재)
브루트포스 + 시뮬레이션
"""
def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    targets = set()
    visited = set()
    visited.add((x, y))
    while queue:
        for _ in range(len(queue)):
            x, y, depth = queue.popleft()
            if depth == D:
                continue
            for dx,dy in zip([-1,0,0],[0,-1,1]):
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<M and (nx,ny) not in visited:
                    if metaverse[nx][ny] == 1:
                        targets.add((nx,ny))
                    else:
                        queue.append((nx,ny,depth+1))
                        visited.add((nx,ny))
            if targets:
                x,y = 0,M-1
                for target in targets:
                    if target[1] <= y:
                        x,y = target
                return (x,y)
    return (-1,-1)


N,M,D = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(N)]
down = N
for line in world:
    if 1 in line:
        break
    down -= 1
new_line = [0]*M
answer = 0
"""
M개 중에서 3개 뽑기 (조합)
"""
for arrows in combinations(range(M),3):
    local_answer = 0
    metaverse = [w[:] for w in world] + [new_line[:]]
    for _ in range(down):
        targets = set()
        for y in arrows:
            targets.add(bfs(N,y))
        for x,y in targets:
            if x != -1 and y != -1 and metaverse[x][y] == 1:
                metaverse[x][y] = 0
                local_answer += 1
        metaverse = metaverse[1:]+[new_line[:]]
    answer = max(answer,local_answer)
print(answer)