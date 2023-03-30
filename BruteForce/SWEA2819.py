import sys
sys.stdin = open('input.txt')

from collections import deque
dx,dy = [1,-1,0,0],[0,0,1,-1]
T = int(input())
for test_case in range(1,1+T):
    answer = set()
    grid = [input().split() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            queue = deque()
            queue.append((i,j,0,grid[i][j]))
            while queue:
                x,y,depth,string = queue.popleft()
                if depth == 6:
                    answer.add(string)
                    continue
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0<=nx<4 and 0<=ny<4:
                        queue.append((nx,ny,depth+1,string+grid[nx][ny]))
    print(f"#{test_case} {len(answer)}")