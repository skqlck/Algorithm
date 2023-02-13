import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    String = input()
    stack = []
    for char in String:
        if char in "({":
            stack.append(char)
        elif char == ")":
            if stack and stack.pop() == "(":
                continue
            else:
                print(f"#{test_case} 0")
                break
        elif char == "}":
            if stack and stack.pop() == "{":
                continue
            else:
                print(f"#{test_case} 0")
                break
    else:
        if stack:
            print(f"#{test_case} 0")
        else:
            print(f"#{test_case} 1")