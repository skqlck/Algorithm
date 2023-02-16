import sys
sys.stdin = open("sample_input.txt","r")
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    # 흑돌 1 백돌 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2

    for _ in range(M):
        y,x,color = map(int,input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        for dx, dy in zip([1, 1, 1, 0, 0, -1, -1, -1], [1, 0, -1, 1, -1, 1, 0, -1]):
            nx,ny = x+dx,y+dy
            while True:
                if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                    break
                if board[nx][ny] == 0:
                    break
                if board[nx][ny] == color:
                    while nx != x or ny != y:
                        nx,ny = nx-dx,ny-dy
                        board[nx][ny] = color
                    break
                nx,ny = nx+dx,ny+dy

    cnt = [0,0]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt[0] += 1
            elif board[i][j] == 2:
                cnt[1] += 1

    print(f"#{test_case} {cnt[0]} {cnt[1]}")

