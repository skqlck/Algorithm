import sys
sys.stdin = open('input.txt')
def calculate(depth,cal):
    global opers
    global minimum
    global maximum
    if depth == N:
        if maximum < cal:
            maximum = cal
        if minimum > cal:
            minimum = cal
        return

    if opers[0]:
        opers[0] -= 1
        calculate(depth+1,cal+numbers[depth])
        opers[0] += 1

    if opers[1]:
        opers[1] -= 1
        calculate(depth+1,cal-numbers[depth])
        opers[1] += 1

    if opers[2]:
        opers[2] -= 1
        calculate(depth+1,cal*numbers[depth])
        opers[2] += 1

    if opers[3]:
        opers[3] -= 1
        calculate(depth+1,int(cal/numbers[depth]))
        opers[3] += 1

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    opers = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    minimum = 100000000
    maximum = -100000000
    calculate(1,numbers[0])
    print(f'#{test_case} {maximum-minimum}')
