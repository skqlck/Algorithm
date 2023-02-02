from itertools import combinations
T = int(input())
for test_case in range(1,1+T):
    N,K,M = map(int,input().split())
    answer = 0
    for c in combinations(range(1,N+1),K):
        product = 1
        for number in c:
            product *= number
        answer += product%M
    answer %= M
    print(f'#{test_case} {answer}')