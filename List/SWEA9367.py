T = int(input())
for test_case in range(1,1+T):
    answer = 1
    N = int(input())
    carrots = list(map(int,input().split()))
    before = carrots[0]
    cnt = 1
    for i in range(1,N):
        if carrots[i] == before + 1:
            cnt += 1
            if answer < cnt:
                answer = cnt
        else:
            cnt = 1
        before = carrots[i]

    print(f"#{test_case} {answer}")