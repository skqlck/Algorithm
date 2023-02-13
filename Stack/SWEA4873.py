import sys
sys.stdin = open("sample_input.txt","r")
T = int(input())
for test_case in range(1,1+T):
    String = input()
    stack = ''
    flag = True

    while flag:
        flag = False
        for char in String:
            if stack == '':
                stack += char
                continue
            if stack[-1] == char:
                stack = stack[:-1]
                flag = True
                continue
            stack += char
        String = stack
        stack = ''
    print(f"#{test_case} {len(String)}")

