import sys
sys.stdin = open("input.txt","r")
def hoimoon_line(line,start,end):
    while start < end:
        if line[start] == line[end]:
            start += 1
            end -= 1
            continue
        return False
    return True

for test_case in range(1,11):
    M = int(input())
    board = [input() for _ in range(8)]
    answer = 0
    for line in board:
        for i in range(8-M+1):
            if hoimoon_line(line,i,i+M-1):
                answer += 1

    for line in zip(*board):
        line = ''.join(line)
        for i in range(8-M+1):
            if hoimoon_line(line,i,i+M-1):
                answer += 1

    print(f"#{test_case} {answer}")
