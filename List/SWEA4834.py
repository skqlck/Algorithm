T = int(input())
for test_case in range(1,1+T):
    input()
    counts = [0]*10
    numbers = list(map(int,input()))
    for number in numbers:
        counts[number] += 1

    max_num = 0
    max_cnt = 0

    for i in range(10):
        if counts[i] >= max_cnt:
            max_cnt = counts[i]
            max_num = i

    print(f"#{test_case} {max_num} {max_cnt}")