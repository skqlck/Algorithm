"""
조건에 맞는 부분집합 구하기 (부분집합의 합과 크기)
"""
arr = [i for i in range(1,13)]
T = int(input())
for test_case in range(1,1+T):
    N,K = map(int,input().split())
    answer = 0
    for i in range(1<<12):
        total,cnt = 0,0
        for j in range(12):
            if i & (1<<j):
                total += arr[j]
                cnt += 1
                if total > K or cnt > N:
                    break
        if total == K and cnt == N:
            answer += 1
    print(f"#{test_case} {answer}")