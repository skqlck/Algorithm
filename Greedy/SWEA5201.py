T = int(input())
for test_caes in range(1,1+T):
    N,M = map(int,input().split())
    weights = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    weights.sort()
    trucks.sort()
    w_idx = N-1
    t_idx = M-1
    answer = 0
    while t_idx > -1 and w_idx > -1:
        if trucks[t_idx] >= weights[w_idx]:
            answer += weights[w_idx]
            t_idx -= 1
            w_idx -= 1
        else:
            w_idx -= 1
    print(f"#{test_caes} {answer}")