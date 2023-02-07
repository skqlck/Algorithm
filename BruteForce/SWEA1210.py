# import sys
# sys.stdin = open("BruteForce/input.txt","r")

"""
위에서부터 2를 찾는다면 100개 중에 최대 100개를 찾아야하지만,
아래서 2를 찾고 위로 올라간다면 딱 한번만 하면 된다.
"""
for _ in range(10):
    test_case = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    # 도착지에서 출발하기
    x = 99
    for j in range(100):
        if ladder[x][j] == 2:
            y = j
            break

    while x > 0:
        # 왼쪽으로 연결
        if y-1 > -1 and ladder[x][y-1] == 1:
            while y-1 > -1 and ladder[x][y-1] == 1:
                y -= 1
            x -= 1
            continue
        # 오른쪽으로 연결
        if y+1 < 100 and ladder[x][y+1] == 1:
            while y+1 < 100 and ladder[x][y+1] == 1:
                y += 1
            x -= 1
            continue
        x -= 1

    print(f"#{test_case} {y}")


    # 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
    # for i in range(100):
    #     x, y = 0, i
    #     if ladder[x][y] == 1:
    #         while x < 99:
    #             # 왼쪽으로 연결
    #             if y-1 > -1 and ladder[x][y-1] == 1:
    #                 while y-1 > -1 and ladder[x][y-1] == 1:
    #                     y -= 1
    #                 x += 1
    #                 continue
    #             # 오른쪽으로 연결
    #             if y+1 < 100 and ladder[x][y+1] == 1:
    #                 while y+1 < 100 and ladder[x][y+1] == 1:
    #                     y += 1
    #                 x += 1
    #                 continue
    #             x += 1
    #
    #     if ladder[x][y] == 2:
    #         print(f"#{test_case} {i}")
    #         break