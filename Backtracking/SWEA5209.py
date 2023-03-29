def dfs(depth,total):
    global answer
    if answer <= total:
        return
    if depth == N:
        answer = total
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1,total+costs[depth][i])
            visited[i] = 0

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    costs = [list(map(int,input().split())) for _ in range(N)]
    answer = 99*15
    visited = [0]*N
    dfs(0,0)
    print(f"#{test_case} {answer}")