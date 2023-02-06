# import sys
# input = sys.stdin.readline
import math
def balance(left, right, depth):
    global total
    if left >= limit:
        total += 2**(N-depth)*math.factorial(N-depth)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        if left >= right + A[i]:
            balance(left, right + A[i], depth+1)
        balance(left + A[i], right, depth+1)
        visited[i] = 0

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    A = list(map(int,input().split()))
    visited = [0]*len(A)
    limit = sum(A)//2 + sum(A)%2
    total = 0
    for i in range(N):
        visited[i] = 1
        balance(A[i],0,1)
        visited[i] = 0

    print(f"#{test_case} {total}")