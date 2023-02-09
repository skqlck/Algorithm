import sys
sys.stdin = open("sample_input.txt","r")
"""
여는 괄호으로 처음 나오는 닫는 괄호는 무조건 레이저다!!! (괄호가 연속적이기 때문에)
위 사항을 체크하면 큐 필요 X
"""
# from collections import deque
#
# T = int(input())
# for test_case in range(1,1+T):
#     queue = deque()
#     answer = 0
#     for idx,bracket in enumerate(input()):
#         if bracket == "(":
#             queue.append(idx)
#             continue
#
#         if queue[-1] + 1 == idx: # 레이저인 상황
#             queue.pop()
#             answer += len(queue)
#
#         else: # 쇠막대기가 끝나는 상황
#             queue.pop()
#             answer += 1
#
#     print(f"#{test_case} {answer}")
T = int(input())
for test_case in range(1,1+T):
    answer = 0
    sticks = 0
    laser = False
    # laser = True 일때 닫는 괄호가 나오면 무조건 레이저!!!
    for bracket in input():
        if bracket == "(":
            laser = True
            sticks += 1
        else:
            if laser:
                sticks -= 1
                answer += sticks
                laser = False
                continue
            sticks -= 1
            answer += 1
    print(f"#{test_case} {answer}")