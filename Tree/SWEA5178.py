import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N,M,L = map(int,input().split())
    Tree = [0] * (N+1)
    for _ in range(M):
        node,value = map(int,input().split())
        Tree[node] = value

    for node in range(N,1,-1):
        Tree[node//2] += Tree[node]

    print(f'#{test_case} {Tree[L]}')