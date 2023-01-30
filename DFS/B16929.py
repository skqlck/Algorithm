
#import sys
#input = sys.stdin.readline
'''
version_1 500ms
'''
N,M = map(int,input().split())

graph = [list(input()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
check = False
# depth가 3이상일때, 시작노드를 만난다면 싸이클이다!
def get_cycle(x,y,depth):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if depth > 3 and nx == start_x and ny == start_y:
                print('Yes')
                exit(0)

            # 같은 색깔 노드일때
            if graph[nx][ny] == graph[x][y]:
                #미방문 노드일때
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    get_cycle(nx,ny,depth+1)
                    visited[nx][ny] = 0
    return                    
          
for i in range(N): 
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            start_x,start_y = i,j
            get_cycle(i,j,1)
print('No')

'''
version_2 50ms
version_1에 비해 가지치기가 훨씬 잘 되어있다.
'''

# import sys
# input = sys.stdin.readline

n,m=map(int,input().split())
game=[[p for p in input().strip()] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=False
def dfs(x,y,cnt,sx,sy):
    global ans
    if ans:
        return

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if cnt>=4 and sx==nx and sy==ny:
            ans=True
            return True
        if visited[nx][ny]==0 and game[nx][ny]==game[sx][sy]:
            visited[nx][ny]=1
            dfs(nx,ny,cnt+1,sx,sy)
            visited[nx][ny]=0
    return False


def solve():
    global ans
    for i in range(n):
        for j in range(m):
            sx=i
            sy=j
            visited[sx][sy]=True
            dfs(i,j,1,sx,sy)
            if ans:
                return 'Yes'
    return 'No'
print(solve())