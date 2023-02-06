T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    calendar = [[0 for _ in range(N)] for _ in range(N)]
    calendar[0][0] = 1
    x, y = 0, 0
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    idx = 0
    while True:
        nx,ny = x+dx[idx],y+dy[idx]
        if 0 <= nx < N and 0 <= ny < N:
            if not calendar[nx][ny]:
                calendar[nx][ny] = calendar[x][y] + 1
                x,y = nx,ny
                continue
        if calendar[x][y] == N**2:
            break
        nx,ny = x-dx[idx], y-dy[idx]
        idx = (idx+1)%4
    print(f"#{test_case}")
    for row in calendar:
        print(*row)