import sys
sys.stdin = open("sample_input.txt","r")
def distance(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

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
    for k in range(N,0,-1):
        if k**2 + (k-1)**2 <= limit:
            K = k
            break
    else:
        K = 1
    def solution():
        answer = 0
        for k in range(K,0,-1):
            cost = k**2 + (k-1)**2
            for i in range(N):
                for j in range(N):
                    cnt = 0
                    for house in houses:
                        if distance([i,j],house) < K:
                            cnt += 1
                    if cnt > answer and cost <= cnt*M:
                        answer = cnt
                        if answer == len(houses):
                            return answer
        return answer
    answer = solution()
    print(f"#{test_case} {answer}")