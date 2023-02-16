def postfix(expression):
    isp = {'+' : 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+' : 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    result = []
    for char in expression:
        if char.isdigit():
            result.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if stack and isp[stack[-1]] >= icp[char]:
                result.append(stack.pop())
                stack.append(char)
            else:
                stack.append(char)
    while stack:
        result.append(stack.pop())

    return result
def cal(x,y,operation):
    x,y = int(x),int(y)
    if operation == "+":
        return str(x+y)
    if operation == "-":
        return str(x-y)
    if operation == "*":
        return str(x*y)
    if operation == "/":
        return str(x//y)
def cal_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(cal(a,b,char))
    return stack[0]

import sys
sys.stdin = open("input.txt","r")

for test_case in range(1,11):
    input()
    expression = input().strip()
    print(f"#{test_case} {cal_postfix(postfix(expression))}")