T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    ones = input().split('0')
    answer = 0
    for one in ones:
        if len(one) > answer:
            answer = len(one)
    print(f"#{test_case} {answer}")