import sys
sys.stdin = open('input.txt')
from itertools import combinations

def nCr(n,r):
    answer = 1
    for i in range(1,r+1):
        answer *= n
        n -= 1
    for i in range(1,r+1):
        answer //= i
    return answer

def getGap(combination):
    p1,p2 = 0,0
    complement = []
    while p2 < N:
        if combination[p1] == p2:
            if p1 < r-1:
                p1 += 1
            p2 += 1
        else:
            complement.append(p2)
            p2 += 1
    gap = 0
    for i in range(r):
        for j in range(r):
            if i != j:
                gap += Synergy[combination[i]][combination[j]]
                gap -= Synergy[complement[i]][complement[j]]
    return abs(gap)

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    Synergy = [list(map(int,input().split())) for _ in range(N)]
    r = N//2
    limit = nCr(N,r)//2
    answer = 320000
    for i,combination in zip(range(limit),combinations(range(N),r)):
        answer = min(answer, getGap(combination))
    print(f"#{test_case} {answer}")