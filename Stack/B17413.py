'''
스택을 비우는 시기
1. 태그 밖의 space
2. 여는 태그
3. 닫는 태그
이외의 경우엔 스택에 해당 원소 삽입
'''
words = input().strip()
stack = []
tag_chk = False
for char in words:
    if char == '<':
        print(''.join(stack)[::-1], end='')
        stack = []
        tag_chk = True
        stack.append(char)
    elif char == '>':
        tag_chk = False
        stack.append(char)
        print(''.join(stack),end='')
        stack = []
    elif char == ' ':
        if tag_chk:
            stack.append(char)
        else:
            print(''.join(stack)[::-1]+' ', end='')
            stack = []
    else:
        stack.append(char)
if stack:
    print(''.join(stack)[::-1], end='')