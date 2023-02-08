import sys
sys.stdin = open("input.txt","r")

# T = int(input())
for test_case in range(1,11):
    input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    minValue = 10000
    minIdx = -1
    for i in range(100):
        x, y = 0, i
        if ladder[x][y] == 1:
            cnt = 1
            while x < 99:
                if cnt >= minValue:
                    break
                # 왼쪽으로 연결
                if y-1 > -1 and ladder[x][y-1] == 1:
                    while y-1 > -1 and ladder[x][y-1] == 1:
                        y -= 1
                        cnt += 1
                    x += 1
                    cnt += 1
                    continue
                # 오른쪽으로 연결
                if y+1 < 100 and ladder[x][y+1] == 1:
                    while y+1 < 100 and ladder[x][y+1] == 1:
                        y += 1
                        cnt += 1
                    x += 1
                    cnt += 1
                    continue
                x += 1
                cnt += 1
            if minValue > cnt:
                minValue = cnt
                minIdx = i

    print(f"#{test_case} {minIdx}")