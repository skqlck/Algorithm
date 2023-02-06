T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    paper = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                paper[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                cnt += 1
    print(f"#{test_case} {cnt}")
