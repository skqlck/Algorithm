T = int(input())
for test_case in range(1,1+T):
    answer = [0,0,0,0,0]
    numbers = [2,3,5,7,11]
    N = int(input())
    for idx,number in enumerate(numbers):
        while N%number == 0:
            N = N//number
            answer[idx] += 1

    print(f"#{test_case} {' '.join(map(str,answer))}")