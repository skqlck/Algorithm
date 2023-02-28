def kill_mosquito(x,y,k):
    case1 = 0
    for nx in range(x-k+1,x+k):
        if 0 <= nx < N:
            case1 += arr[nx][y]
    for ny in range(y-k+1,y+k):
        if 0<=ny<N:
            case1 += arr[x][ny]
    case1 -= arr[x][y]

    case2 = arr[x][y]
    dx,dy = (1,1,-1,-1),(1,-1,1,-1)
    for i in range(4):
        for s in range(1,k):
            nx,ny = x+s*dx[i],y+s*dy[i]
            if 0<=nx<N and 0<=ny<N:
                case2 += arr[nx][ny]
    return max(case1,case2)

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            answer = max(answer,kill_mosquito(i,j,M))
    print(f"#{test_case} {answer}")