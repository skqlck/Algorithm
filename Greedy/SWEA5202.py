T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    schedules = [list(map(int,input().split())) for _ in range(N)]
    schedules.sort(key=lambda x: x[1])
    answer = 0
    end = 0
    for schedule in schedules:
        if end <= schedule[0]:
            answer += 1
            end = schedule[1]
    print(f"#{test_case} {answer}")