"""
더 디테일하게 라인마다 회문 크기를 측정해서
현재 회문 크기의 최대값을 제한사항으로 걸어버리면
시간이 훨씬 단축된다.
"""
import sys
sys.stdin = open("input.txt","r")
# def hoimoon_block(N,M):
#     for i in range(N):
#         for j in range(N - M + 1):
#             line = board[i][j:j + M]
#             if line == line[::-1]:
#                 return True
#
#     for line in zip(*board):
#         line = ''.join(line)
#         for j in range(N - M + 1):
#             sub = line[j:j + M]
#             if sub == sub[::-1]:
#                 return True
#     return False
#
# for test_case in range(1,11):
#     input()
#     board = [input() for _ in range(100)]
#
#     for M in range(100,0,-1):
#         if hoimoon_block(100,M):
#             print(f"#{test_case} {M}")
#             break
def hoimoon_line(line,start,end):
    while start < end:
        if line[start] == line[end]:
            start += 1
            end -= 1
            continue
        return False
    return True


for test_case in range(1, 11):

    input()
    board = [input() for _ in range(100)]
    answer = 1
    for line in board:
        for start in range(99):
            for end in range(99, start + answer - 1, -1):
                if line[start] == line[end]:
                    if hoimoon_line(line, start, end):
                        answer = end - start + 1

    for line in zip(*board):
        line = ''.join(line)
        for start in range(99):
            for end in range(99, start + answer - 1, -1):
                if line[start] == line[end]:
                    if hoimoon_line(line, start, end):
                        answer = end - start + 1

    print(f"#{test_case} {answer}")


