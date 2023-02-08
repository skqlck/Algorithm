import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    board = [input() for _ in range(N)]

    def hoimoon():
        for i in range(N):
            for j in range(N-M+1):
                line = board[i][j:j+M]
                if line == line[::-1]:
                    return line

        for line in zip(*board):
            line = ''.join(line)
            for j in range(N-M+1):
                sub = line[j:j+M]
                if sub == sub[::-1]:
                    return sub

    print(f"#{test_case} {hoimoon()}")