import sys
sys.stdin = open('input.txt')

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x,y):
    parent[find(y)] = find(x)

T = int(input())
for testCase in range(1,1+T):
    N,M = map(int,input().split())
    parent = [i for i in range(N+1)]
    for _ in range(M):
        u,v = map(int,input().split())
        union(u,v)

    cnt = 0
    for i in range(1,N+1):
        if parent[i] == i:
            cnt += 1
    print(f"#{testCase} {cnt}")