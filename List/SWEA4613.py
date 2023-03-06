import sys
sys.stdin = open("sample_input.txt","r")
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    flag = [input().rstrip() for _ in range(N)]
    answer = N*M+1
    for i in range(N-2):
        for j in range(i+2,N):
            cnt = 0
            for w in range(i+1):
                for c in range(M):
                    if flag[w][c] != "W":
                        cnt += 1
            for b in range(i+1,j):
                for c in range(M):
                    if flag[b][c] != "B":
                        cnt += 1
            for r in range(j,N):
                for c in range(M):
                    if flag[r][c] != "R":
                        cnt += 1
            answer = min(answer,cnt)
    print(f"#{test_case} {answer}")