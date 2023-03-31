import sys
sys.stdin = open('input.txt')

from collections import deque
dx,dy = [-1,1,0,0],[0,0,-1,1]
T = int(input())
for test_case in range(1,1+T):
    N,M,K = map(int,input().split())
    graph = [[0 for  _ in range(N)] for _ in range(N)]
    queue = deque()
    for _ in range(K):
        x,y,k,d = map(int,input().split())
        graph[x][y] = [k,d]
        queue.append((x,y))
    for _ in range(M):
        for _ in range(len(queue)):
