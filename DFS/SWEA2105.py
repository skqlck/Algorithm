import sys
sys.stdin = open('input.txt')

def check(x1,x2,x3,x4,y1,y2,y3,y4):
    global answer
    visited = [0]*101
    cnt = 0
    for x,y in zip(range(x1,x3),range(y1,y3)):
        if visited[graph[x][y]]:
            return
        visited[graph[x][y]] = 1
        cnt += 1
    for x,y in zip(range(x3,x4),range(y3,y4,-1)):
        if visited[graph[x][y]]:
            return
        visited[graph[x][y]] = 1
        cnt += 1
    for x,y in zip(range(x4,x2,-1),range(y4,y2,-1)):
        if visited[graph[x][y]]:
            return
        visited[graph[x][y]] = 1
        cnt += 1
    for x,y in zip(range(x2,x1,-1),range(y2,y1)):
        if visited[graph[x][y]]:
            return
        visited[graph[x][y]] = 1
        cnt += 1
    answer = max(answer,cnt)
    return

T = int(input())
D = ((1,1),(1,-1))
for test_case in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    answer = -1
    for i in range(N):
        for j in range(N):
            x1,y1 = i,j
            for k1 in range(1,N):
                x2,y2 = x1+D[1][0]*k1, y1+D[1][1]*k1
                if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N:
                    break
                for k2 in range(1,N):
                    x3,y3 = x1+D[0][0]*k2, y1+D[0][1]*k2
                    x4,y4 = x2+D[0][0]*k2, y2+D[0][1]*k2
                    if x3 < 0 or x3 >= N or y3 < 0 or y3 >= N:
                        break
                    if x4 < 0 or x4 >= N or y4 < 0 or y4 >= N:
                        break
                    check(x1,x2,x3,x4,y1,y2,y3,y4)
    print(f"#{test_case} {answer}")