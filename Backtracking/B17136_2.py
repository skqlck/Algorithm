import heapq
def can_attach(x,y,k):
    for nx in range(x,x+k):
        for ny in range(y,y+k):
            if 0 > nx or 0 > ny or nx >= 10 or ny >= 10:
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

def dfs(depth, cnt, idx):
    global answer
    if idx == len(heap):
        return
    if answer <= depth:
        return
    if cnt == 0:
        answer = depth

    k,x,y = heap[idx]
    if color_paper[-k] and can_attach(x, y, -k):
        attach(x, y, -k)
        color_paper[-k] -= 1
        dfs(depth + 1, cnt - k ** 2,idx+1)
        detach(x, y, -k)
        color_paper[-k] += 1
    else:
        dfs(depth, cnt, idx + 1)


paper = [list(map(int,input().split())) for _ in range(10)]
total = 0
heap = []
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            total += 1
            for k in range(5,0,-1):
                heapq.heappush(heap,(-k,i,j))
color_paper = [0,5,5,5,5,5]
answer = 25
dfs(0,total,0)
print(answer)
# while heap:
#     visited = [[0] * 10 for _ in range(10)]
#     temp = heap[:]
#     answer = 0
#     cnt = 0
#     for _ in range(len(temp)):
#         k,x,y = heapq.heappop(temp)
#         if color_paper[-k] and can_attach(x,y,-k):
#             attach(x,y,-k)
#             color_paper[-k] -= 1
#             cnt += k**2
#             answer += 1
#         if cnt == total:
#             print(answer)
#             break
#     if cnt == total:
#         break
#     heapq.heappop(heap)
# else:
#     print(-1)
