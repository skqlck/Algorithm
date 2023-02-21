from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if visited[nx][ny]:
                    continue
                if maze[nx][ny] == 3:
                    return True
                elif maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    else:
        return False

for test_case in range(1,11):
    input()
    maze = [list(map(int,input())) for _ in range(16)]
    flag = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                x,y = i,j
                flag = True
                break
        if flag:
            break

    visited = [[0 for _ in range(16)] for _ in range(16)]
    visited[x][y] = 1
    if bfs(x,y):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")