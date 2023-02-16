T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    corridor = [0]*200
    for _ in range(N):
        start,end = map(int,input().split())
        if start > end:
            start,end = end,start
        start -= 1
        end -= 1
        for i in range(start//2,end//2+1):
            corridor[i] += 1
    print(f"#{test_case} {max(corridor)}")