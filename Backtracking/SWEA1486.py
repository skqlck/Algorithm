import sys
sys.stdin = open('../BItOperation/input.txt')
def backtracking(depth,height):
    global answer
    if height >= answer:
        return

    if depth == N:
        if height >= B:
            answer = height
        return

    backtracking(depth+1,height+H[depth])
    backtracking(depth+1,height)

T = int(input())
for test_case in range(1,1+T):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    answer = sum(H)
    backtracking(0,0)
    print(f"#{test_case} {answer-B}")