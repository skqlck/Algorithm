import sys
sys.stdin = open("input2.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    points = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for x in range(N):
        for y in range(M):
            cnt = 0
            for dx,dy in zip([1,1,1,0,0,-1,-1,-1],[1,0,-1,1,-1,1,0,-1]):
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<M:
                    if points[x][y] > points[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                answer += 1

    print(f"#{test_case} {answer}")