def subset(N,K,start):
    global cnt
    if N == 0 and K == 0:
        cnt += 1
        return
    for i in range(start,13):
        if K >= i:
            subset(N-1,K-i,i+1)

T = int(input())
for test_case in range(1,1+T):
    N,K = map(int,input().split())
    if K > 78:
        print(f"#{test_case} {0}")
    else:
        cnt = 0
        subset(N,K,1)
        print(f"#{test_case} {cnt}")
