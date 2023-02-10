import sys
sys.stdin = open("input.txt","r")
def product(A,B):
    total = 0
    for a,b in zip(A,B):
        total += a*b
    return total
def compare(a,b):
    if a > b:
        return a
    else:
        return b
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    answer = 0
    if N > M:
        A,B = B,A
        N,M = M,N
    for i in range(M-N+1):
        answer = compare(product(A,B[i:i+M]),answer)
    print(f"#{test_case} {answer}")
