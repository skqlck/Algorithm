import sys
sys.stdin = open("sample_input.txt","r")
def solution():
    answer = 0
    for k in range(K,0,-1):
        cost = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for house in houses:
                    if abs(i-house[0]) + abs(j-house[1]) < k:
                        cnt += 1
                if cost <= cnt*M and answer < cnt:
                    answer = cnt
                    if answer == len(houses):
                        return answer
    return answer

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    houses = tuple()
    for i in range(N):
        line = list(map(int,input().split()))
        for j in range(N):
            if line[j] == 1:
                houses += ((i,j),)
    limit = M*len(houses)
    for k in range(N+1,0,-1):
        if k**2 + (k-1)**2 <= limit:
            K = k
            break
    else:
        K = 1
    answer = solution()
    print(f"#{test_case} {answer}")