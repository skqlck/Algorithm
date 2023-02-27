from collections import deque
N,M = map(int,input().split())
graph = [list(map(lambda x : -int(x),input().split())) for _ in range(N)]
group_num = 0
dx,dy = [1,-1,0,0],[0,0,1,-1]
edge_of_islands = [0]

# 섬들 나누기
for i in range(N):
    for j in range(M):
        if graph[i][j] == -1:
            group_num += 1
            graph[i][j] = group_num
            edge_of_island = set()
            queue = deque()
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] == -1:
                            graph[nx][ny] = group_num
                            queue.append((nx,ny))
                        elif graph[nx][ny] == 0:
                            edge_of_island.add((x,y,k))
            edge_of_islands.append(edge_of_island)

# for line in graph:
#     print(line)
# 섬들 간 거리 구하기
groups = list(range(group_num+1))
distances = [[100 for _ in range(group_num+1)] for _ in range(group_num+1)]
for island in range(1,group_num+1):
    for x,y,k in edge_of_islands[island]:
        nx,ny = x+dx[k],y+dy[k]
        distance = 0
        while 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]  == 0:
                nx,ny = nx+dx[k],ny+dy[k]
                distance += 1
            elif graph[nx][ny] == island:
                break
            else:
                if distance > 1:
                    distances[island][graph[nx][ny]] = min(distances[island][graph[nx][ny]],distance)
                break
# for line in distances:
#     print(line)
distances_list = []
for i in range(1,group_num):
    for j in range(i+1,group_num+1):
        if i != j and distances[i][j] < 100:
            distances_list.append((distances[i][j],i,j))
def get_group(x):
    if groups[x] == x:
        return x
    return get_group(groups[x])

distances_list.sort(key=lambda x : x[0])
cnt = 0
total = 0
for dist,x,y in distances_list:
    if get_group(x) != get_group(y):
        groups[get_group(y)] = get_group(x)
        cnt += 1
        total += dist
    if cnt == group_num-1:
        print(total)
        break
else:
    print(-1)
# print(edge_of_islands)
# for line in graph:
#     print(line)
# for line in distances:
#     print(line)