import sys
sys.stdin = open('input.txt')

dx,dy = [-1,1,0,0],[0,0,-1,1]
T = int(input())
for test_case in range(1,1+T):
    N,M,K = map(int,input().split())
    minHeap = []
    Before = [[0 for _ in range(N)] for _ in range(N)]
    After = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        x,y,k,direction = map(int,input().split())
        minHeap.append((x,y))
        Before[x][y] = [k,direction-1]

    for _ in range(M):
        minHeap.sort(key = lambda x : Before[x[0]][x[1]])
        newHeap = []
        for _ in range(len(minHeap)):
            x,y = minHeap.pop()
            k,direction = Before[x][y]
            nx,ny = x+dx[direction], y+dy[direction]
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                k //= 2
                if direction%2 == 0: # 0과 2 인덱스 -> 1과 3 인덱스
                    direction += 1
                else:
                    direction -= 1
            Before[x][y] = 0
            if k:
                if After[nx][ny] == 0:
                    After[nx][ny] = [k,direction]
                    newHeap.append((nx,ny))
                else:
                    After[nx][ny][0] += k
        Before,After = After, Before
        minHeap = newHeap[:]
    answer = 0
    for x,y in minHeap:
        if Before[x][y] != 0:
            answer += Before[x][y][0]
    print(f"#{test_case} {answer}")