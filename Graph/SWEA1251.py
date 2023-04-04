import sys
sys.stdin = open('input.txt')

def prim():
    answer = 0
    U = [0]*N
    D = [2e12] * N
    D[0] = 0
    for _ in range(N):
        minV = 2e12
        for i in range(N):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                v = i

        U[v] = 1
        answer += D[v]

        for w in range(N):
            if U[w]:
                continue
            D[w] = min(D[w], distance(v,w))
    return answer

def distance(i,j):
    x1, y1 = X[i], Y[i]
    x2, y2 = X[j], Y[j]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

T = int(input())
for testCase in range(1,1+T):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    print(f"#{testCase} {round(E*prim())}")