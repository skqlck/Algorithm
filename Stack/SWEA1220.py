for test_case in range(1,11):
    input()
    magnetics = [list(map(int,input().split())) for _ in range(100)]
    answer = 0

    for j in range(100):
        stack = []
        cnt = 0
        for i in range(100):
            # 1은 N극 2는 S극
            if magnetics[i][j] == 1:
                stack.append(1)
            elif magnetics[i][j] == 2:
                if stack:
                    if stack[-1] == 1:
                        cnt += 1
                    stack.append(2)
        answer += cnt
    print(f"#{test_case} {answer}")