def backtrack(local_sum,depth):
    global answer
    if depth == N:
        answer = min(local_sum, answer)
        return

    for i in range(N):
        if not visited[i] and local_sum + arr[depth][i] < answer:
            visited[i] = 1
            backtrack(local_sum + arr[depth][i],depth+1)
            visited[i] = 0


T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    answer = 100
    backtrack(0,0)
    print(f"#{test_case} {answer}")