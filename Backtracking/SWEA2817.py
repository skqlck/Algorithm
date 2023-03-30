def subset(depth,total,rest):
    global answer
    if rest+total < K:
        return
    if total > K:
        return
    if total == K:
        answer += 1
        return
    if depth == N:
        return
    rest -= A[depth]
    subset(depth+1,total+A[depth],rest)
    subset(depth+1,total,rest)

T = int(input())
for test_case in range(1,1+T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    sum_A = sum(A)
    answer = 0
    subset(0,0,sum_A)
    print(f"#{test_case} {answer}")
