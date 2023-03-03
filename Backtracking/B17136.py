def can_attach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            if nx > 9 or ny > 9:
                return False
            if paper[nx][ny] == 0:
                return False
    return True
def attach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            paper[nx][ny] = 0
def detach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            paper[nx][ny] = 1

def dfs(x,y,depth,cnt):
    global answer
    if depth >= answer:
        return
    if cnt == 0:
        answer = min(depth, answer)
        return

    if paper[x][y] == 1:
        for k in range(5,0,-1):
            if color_paper[k] and can_attach(x,y,k):
                attach(x,y,k)
                color_paper[k] -= 1
                if y+k < 10:
                    dfs(x, y+k, depth+1, cnt-k**2)
                elif x < 9:
                    dfs(x+1, 0, depth+1, cnt-k**2)
                else:
                    answer = min(depth+1,answer)
                detach(x,y,k)
                color_paper[k] += 1
    else:
        if y<9:
            dfs(x,y+1,depth,cnt)
        elif x<9:
            dfs(x+1,0,depth,cnt)

paper = [list(map(int,input().split())) for _ in range(10)]
total = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            total += 1
color_paper = [0,5,5,5,5,5]
answer = 25
dfs(0,0,0,total)
if answer == 25:
    print(-1)
else:
    print(answer)