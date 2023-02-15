import sys
sys.stdin = open("sample_input.txt","r")
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

T = int(input())
for test_case in range(1,1+T):
    expression = input().split()
    stack = []

    for char in expression:
        if char == '.':
            break
        if char.isdigit():
            stack.append(char)
        else:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                stack.append(cal(a,b,char))
            else:
                stack = [0,0]
                break
    if len(stack) != 1:
        print(f"#{test_case} error")
    else:
        print(f"#{test_case} {stack.pop()}")
