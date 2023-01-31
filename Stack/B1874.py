'''
스택대로 하면 된다.
Push 조건
- 스택이 비었을 때
- 수열의 숫자가 스택의 마지막 원소보다 클 때
Pop 조건
- 스택의 마지막 원소가 수열의 숫자와 같을 때
만약 수열의 숫자가 스택의 마지막 숫자보다 작다면 수열을 만들 수 없다!
==> 그리디와 매우 흡사
'''
from collections import deque

def stack_seq(N,sequence):
    answer = []
    stack = deque()
    cnt = 1
    for i in range(N):
        n = sequence[i]
        while True:
            if not stack:
                answer.append('+')
                stack.append(cnt)
                cnt += 1

            elif stack[-1] == n:
                stack.pop()
                answer.append('-')
                break

            elif stack[-1] < n:
                stack.append(cnt)
                answer.append('+')
                cnt += 1
            
            else:
                print('NO')
                return
    for a in answer:
        print(a)
    return

N = int(input())
sequence = [int(input()) for _ in range(N)]
stack_seq(N,sequence)       