def check(x,y):
    ly,ry = y,y
    while x >= 0:
        x -= 1
        if graph[x][y] == 1:
            return False
        if ly > 0:
            ly -= 1
            if graph[x][ly] == 1:
                return False
        if ry < N-1:
            ry += 1
            if graph[x][ry] == 1:
                return False
    return True
def N_Queens(row,depth):
    global cnt
    if depth == N:
        cnt += 1
    for i in range(row,N):
        for j in range(N):
            if check(i,j):
                graph[i][j] = 1
                N_Queens(i+1,depth+1)
                graph[i][j] = 0
    return

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    cnt = 0
    graph = [[0 for _ in range(N)] for _ in range(N)]
    N_Queens(0,0)
    print(f"#{test_case} {cnt}")