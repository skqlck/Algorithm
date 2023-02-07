"""
예를 들어, 가로선에 정확히 K개의 빈칸이 있는지 센다면
[x][y] [x][y+1] ... [x][y+K-1] 뿐만 아니라,
※ [x][y+K]와 [x][y-1]도 빈칸인지 확인해야한다.
"""
# import sys
# sys.stdin = open("List/input.txt","r")

def horizontal(x,y):
    if y > N-K:
        return False
    for k in range(K):
        if not puzzle[x][y+k]:
            return False
    if y+K < N:
        if puzzle[x][y+K]:
            return False
    if y > 0 and puzzle[x][y-1]:
        return False

    return True

def vertical(x,y):
    if x > N-K:
        return False
    for k in range(K):
        if not puzzle[x+k][y]:
            return False
    if x+K < N:
        if puzzle[x+K][y]:
            return False
    if x > 0 and puzzle[x-1][y]:
        return False

    return True

T = int(input())
for test_case in range(1,1+T):
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j]:
                cnt += horizontal(i,j) + vertical(i,j)
    print(f"#{test_case} {cnt}")