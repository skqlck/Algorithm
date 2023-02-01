for test_case in range(1,11):
    N = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    idx = 2
    while idx < N-2:
        min_gap = 255
        for near in [idx-2,idx-1,idx+1,idx+2]:
            gap = buildings[idx] - buildings[near]
            if gap <= 0:
                idx += 1
                break
            if min_gap > gap:
                min_gap = gap
        else:
            cnt += min_gap
            idx += 3
    print(f"#{test_case} {cnt}")