def backtracking(depth,row,local_answer):
    global answer
    if local_answer >= answer:
        return
    
    if depth == N-1:
        answer = min(answer,local_answer + graph[row][0])
        return
    
    for i in range(1,N):
        if i != row and not visited[i]:
            visited[i] = 1
            backtracking(depth+1, i, local_answer + graph[row][i])
            visited[i] = 0

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    answer = 5000
    visited = [0]*N
    backtracking(0,0,0)
    print(f"#{test_case} {answer}")