import sys
sys.stdin = open('List/input.txt','r')
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    paris = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            local_answer = sum(sum(paris[i+k][j:j+M]) for k in range(M))
            if local_answer > answer:
                answer = local_answer
    print(f"#{test_case} {answer}")
