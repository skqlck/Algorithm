from collections import deque
from itertools import combinations
def find_enemy(start_x,start_y,depth):
    visited = set()
    targets = set()
    queue = deque()
    queue.append((start_x,start_y,depth))
    visited.add((start_x,start_y,depth))
    while queue:
        for same_level in range(len(queue)):
            x,y,depth = queue.popleft()
            if depth == 0:
                nx,ny = x-1,y
                if metaverse[nx][ny] == 1:
                    targets.add((nx, ny))
                    visited.add((nx, ny))
                else:
                    visited.add((nx, ny))
                    queue.append((nx, ny, depth + 1))
            elif depth < D:
                for dx,dy in zip([0,-1,0],[-1,0,1]):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<M and (nx,ny) not in visited:
                        if metaverse[nx][ny] == 1:
                            targets.add((nx,ny))
                            visited.add((nx,ny))
                        else:
                            visited.add((nx,ny))
                            queue.append((nx,ny,depth+1))
            if targets:
                return sorted(targets,key=lambda x : x[1])[0]
    return 0

N,M,D = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for arrows in combinations(range(M),3):
    metaverse = [world[i][:] for i in range(N)] + [[0] * M]
    local_max = 0
    for time_goes in range(N,0,-1):
        targets = set()
        for arrow in arrows:
            new_target = find_enemy(time_goes,arrow,0)
            if new_target != 0:
                targets.add(new_target)
        for target in targets:
            metaverse[target[0]][target[1]] = 0
            local_max += 1
    answer = max(answer,local_max)
print(answer)
