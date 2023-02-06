def dfs(N,K):
    global answer
    if sorted(N,reverse=True) == N:
        if K%2 == 0:
            pass
        else:
            N[-1],N[-2] = N[-2],N[-1]
        answer = max(answer,N)
        return

    if K == 0:
        if answer < N:
            answer = N
            return

    for i in range(len(N)-1,0,-1):
        for j in range(i-1,-1,-1):
            if not visited[i] and not visited[j]:
                if N[i] < N[j]:
                    N[i],N[j] = N[j],N[i]
                    visited[i] = 1
                    visited[j] = 1
                    dfs(N,K-1)
                    visited[i] = 0
                    visited[j] = 0
                    N[i], N[j] = N[j], N[i]

T = int(input())
for test_case in range(1,1+T):
    N, K = input().split()
    K = int(K)
    answer = '0'
    visited = [0]*len(N)
    dfs(N,K)
    print(f"#{test_case} {answer}")
