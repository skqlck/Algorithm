'''
한 벽을 허물었을때, 주위에 벽이 아닌 곳과 연결된 만큼 갈 수 있다.
즉, 어떠한 벽도 허물지 않은 상태로 붙어있는 0들의 개수들을 구한 후
이를 이용하여 벽을 부쉈을 때, 주위의 0의 그룹 수만큼 더해주면 된다.
주위 + 1 == 현재 벽을 부쉈을 때, 가능한 것
str(1)이면 벽이고! str(0)이면 아직 그룹핑이 안된 빈칸!
'''
#import sys
#input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

def bfs(x,y,group_num):
    cnt = 0
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == '0':
                    queue.append([nx,ny])
                    graph[nx][ny] = group_num
    return cnt

group_cnt = []
group_num = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            graph[i][j] = group_num
            group_cnt.append(bfs(i,j,group_num))
            group_num += 1

def nearby(x,y):
    groups = set()
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] != '1':
                groups.add(graph[nx][ny])
    return sum(map(lambda x: group_cnt[x],groups)) + 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == '1':
            print(nearby(i,j)%10,end='')
        else:
            print('0',end='')
    print()
