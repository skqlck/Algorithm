def backtracking(depth,probability):
    global answer
    if answer >= probability:
        return

    if depth == N:
        answer = probability

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtracking(depth+1, probability*jobs[depth][i])
            visited[i] = 0

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    jobs = [list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]
    visited = [0]*N
    answer = 0
    backtracking(0,1)
    print(f"#{test_case}","{:0.6f}".format(answer*100))
