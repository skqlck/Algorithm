"""
봄 - 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    가장 어린 나무부터, 양분 < 나이 -> 죽음

여름 - 죽은 나무의 나이 // 2만큼 양분 추가 (해당 지점에만)

가을 - 나이가 5배수인 나무는 인접 8칸에 번식 (나이가 1인 나무)

겨울 - S2D2가 땅을 돌아다니면서 양분 추가
"""
import sys
input = sys.stdin.readline
from collections import deque
N,M,K = map(int,input().split())
farm = [[5 for _ in range(N)] for _ in range(N)]
A = [list(map(int,input().split())) for _ in range(N)]
trees = [[ [] for _ in range(N)] for _ in range(N)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(M):
    x,y,age = map(int,input().split())
    trees[x-1][y-1].append(age)

for i in range(N):
    for j in range(N):
        trees[i][j].sort()
        trees[i][j] = deque(trees[i][j])

for _ in range(K):
    # 봄
    for x in range(N):
        for y in range(N):
            nutrition = 0
            grow = []
            for _ in range(len(trees[x][y])):
                age = trees[x][y].popleft()
                if farm[x][y] >= age:
                    farm[x][y] -= age
                    trees[x][y].append(age+1)
                else:
                    nutrition += age//2
            farm[x][y] += nutrition + A[x][y]

    # 여름

    # 가을
    for x in range(N):
        for y in range(N):
            for age in trees[x][y]:
                if age % 5:
                    continue
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        trees[nx][ny].appendleft(1)

    #겨울

answer = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            answer += len(trees[i][j])
print(answer)
