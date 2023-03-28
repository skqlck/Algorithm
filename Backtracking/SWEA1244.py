def swap(String,a,b):
    ls = list(String)
    ls[a],ls[b] = ls[b],ls[a]
    return ''.join(ls)

def backtrack(M,depth):
    global answer

    if depth == K:
        answer = max(answer,M)
        return

    for i in range(n-1):
        for j in range(i+1,n):
            newM = swap(M,i,j)
            if newM not in visited[depth+1]:
                visited[depth+1].add(newM)
                backtrack(newM,depth+1)

T = int(input())
for test_case in range(1,1+T):
    N,K = input().split()
    K = int(K)
    n = len(N)
    if K%2:
        answer = swap(N, 0, 1)
    else:
        answer = N
    visited = {k: set() for k in range(1,K+1)}
    backtrack(N,0)
    print(f"#{test_case} {answer}")