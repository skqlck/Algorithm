def can_attach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            if 0 > nx or 0 > ny or nx >= 10 or ny >= 10:
                return False
            if paper[nx][ny] == 0:
                return False
            if visited[nx][ny]:
                return False
    return True
def attach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            visited[nx][ny] = 1
def detach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            visited[nx][ny] = 0
def dfs(depth,cnt):
    global answer
    if depth >= answer:
        return
    if cnt == total:
        answer = min(answer,depth)
        return
    for x in range(10):
        for y in range(10):
            if paper[x][y] == 1 and not visited[x][y]:
                for k in range(5,0,-1):
                    if color_paper[k] and can_attach(x,y,k):
                        attach(x,y,k)
                        color_paper[k] -= 1
                        dfs(depth+1,cnt+k**2)
                        detach(x,y,k)
                        color_paper[k] += 1

paper = [list(map(int,input().split())) for _ in range(10)]
total = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            total += 1
color_paper = [0,5,5,5,5,5]
visited = [[0]*10 for _ in range(10)]
answer = 25
if total:
    for x in range(10):
        for y in range(10):
            if paper[x][y] == 1:
                for k in range(5,0,-1):
                    if color_paper[k] and can_attach(x,y,k):
                        attach(x,y,k)
                        color_paper[k] -= 1
                        dfs(1,k**2)
                        detach(x,y,k)
                        color_paper[k] += 1
                    print(*visited)
                if answer == 25:
                    print(-1)
                else:
                    print(answer)
                exit(0)
else:
    print(0)