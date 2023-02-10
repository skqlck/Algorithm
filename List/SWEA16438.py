import sys
sys.stdin = open("input.txt","r")
"""
범위 내에 있다면 무조건 이동
범위 밖을 향한다면 방향전환 dx,dy -> -dx,-dy
"""
T = int(input())
for test_case in range(1,1+T):
    N,M,K,x,y = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    dust = graph[x][y]
    graph[x][y] = 0
    for _ in range(K):
        # 0,1,2,3 => 상 하 좌 우
        direction,steps = map(int,input().split())
        dx,dy = delta[direction]
        while steps:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                x,y = nx,ny
                dust += graph[nx][ny]
                graph[nx][ny] =0
                steps -= 1
            else:
                dx,dy = -dx,-dy

    print(f"#{test_case} {dust} {x} {y}")

