from collections import deque
maze = [list(input()) for _ in range(8)]
D = [[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1],[-1,-1],[-1,0],[-1,1]]
'''
움직이는 벽을 미로 상에서 표기해놓는 것이 아니라, set에 벽 좌표를 입력해서
이를 이용하여 이동함. set을 사용하는 이유는 x in set이 x in list보다 빠르고
벽의 수가 많지 않기 때문
'''
walls = set()
for i in range(8):
    for j in range(8):
        if maze[i][j] == '#':
            walls.add((i,j))
'''
현재의 벽과 한 타임 이후 벽의 위치를 알면, 현재 갈 수 없는 곳에 대한 가지치기를
더 잘할 수 있다. 그래서 미리 움직일 벽의 위치를 알아내서 이를 이용
'''
def move_walls(walls):
    moving_walls = set()
    for x,y in walls:
        if x < 7:
            moving_walls.add((x+1,y))
    return moving_walls
moving_walls = move_walls(walls)

'''
visited를 사용하는 이유는 현재 위치에 다시 방문할 수는 있지만(꼭 필요한 경우도 존재),
현재 스텝에서 같은 위치를 여러번 밟는 것(서로 다른 위치에서 한 지점으로 움직이는 것)은
중복이므로 제거하기위해 visited를 사용 -> 한 스텝이 끝나면 visited는 초기화
'''
def bfs(walls,moving_walls):
    queue = deque()
    queue.append([7,0])
    while queue:
        visited = set()
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for dx,dy in D:
                nx,ny = x+dx,y+dy
                if 0<=nx<8 and 0<=ny<8:
                    if [nx,ny] == [0,7]:
                        return 1
                    if (nx,ny) in walls:
                        continue
                    if (nx,ny) in moving_walls:
                        continue
                    if (nx,ny) in visited:
                        continue
                    queue.append([nx,ny])
                    visited.add((nx,ny))
        walls = moving_walls
        moving_walls = move_walls(walls)
    return 0

print(bfs(walls,moving_walls))