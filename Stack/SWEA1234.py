import sys
sys.stdin = open("input.txt","r")

for test_case in range(1,11):
    stack = []
    N, password = input().split()

    for p in password:
        if (stack and stack[-1] != p) or not stack:
            stack.append(p)
        elif stack[-1] == p:
            stack.pop()

    print(f"#{test_case} {''.join(stack)}")