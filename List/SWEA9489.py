import sys
sys.stdin = open("input1.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    photo = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for line in photo:
        cnt = 0
        for elem in line:
            if elem == 1:
                cnt += 1
            else:
                answer = max(cnt,answer)
                cnt = 0
        answer = max(cnt, answer)
    for line in zip(*photo):
        cnt = 0
        for elem in list(line):
            if elem == 1:
                cnt += 1
            else:
                answer = max(cnt,answer)
                cnt = 0
        answer = max(cnt, answer)
    print(f"#{test_case} {answer}")
