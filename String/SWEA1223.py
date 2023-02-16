import sys
sys.stdin = open("input.txt","r")

def mul(arr):
    answer = 1
    for element in arr:
        answer *= element
    return answer

for test_case in range(1,11):
    input()
    expression = input().strip()
    expression = expression.split('+')
    answer = 0
    for exp in expression:
        if len(exp) == 1:
            answer += int(exp)
        else:
            a = list(map(int,exp.split('*')))
            answer += mul(a)
    print(f"#{test_case} {answer}")