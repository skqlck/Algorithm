T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    counts = [0]*N
    A = list(map(int,input().split())) # len(A) = N
    B = list(map(int,input().split())) # len(B) = M
    for b in B:
        for i in range(N):
            if A[i] <= b:
                counts[i] += 1
                break

    max_cnt = 0
    answer = 0
    for i in range(N):
        if max_cnt < counts[i]:
            max_cnt = counts[i]
            answer = i
    print(f"#{test_case} {answer+1}")