from collections import deque

N,L,R = map(int,input().split())
populations = [list(map(int,input().split())) for _ in range(N)]
groups = [[0 for _ in range(N)] for _ in range(N)]
group_mean = [0]
group_num = 1
days = 0

def bfs(x, y, group_num): # 그룹별로 그루핑하고, 평균값 반환, 그룹이 안된다면 0 반환
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    queue.append([x,y])
    group_cnt = 1
    group_sum = populations[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if groups[nx][ny]:
                continue
            if L <= abs(populations[x][y] - populations[nx][ny]) <= R:
                queue.append([nx,ny])
                groups[nx][ny] = group_num
                group_sum += populations[nx][ny]
                group_cnt += 1
    return group_sum//group_cnt if group_cnt != 1 else 0

while True:
    for i in range(N):
        for j in range(N):
            if not groups[i][j]:
                groups[i][j] = group_num
                local_mean = bfs(i, j, group_num)
                # 그룹핑이 안됐다면, 그룹 넘버 갱신X
                if local_mean == 0:
                    groups[i][j] = 0
                    continue

                group_mean.append(local_mean)
                group_num += 1

    for i in range(N):
        for j in range(N):
            if groups[i][j]:
                populations[i][j] = group_mean[groups[i][j]]
                groups[i][j] = 0

    # group_num == 1 <=> 그룹이 나눠지지 않았다.
    if group_num == 1:
        break

    days += 1
    group_mean = [0]
    group_num = 1

pprint(populations)
print(days)


