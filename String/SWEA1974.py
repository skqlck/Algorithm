import sys
sys.stdin = open("input.txt","r")
def check_sudoku(sudoku):
    true_set = set(range(1,10))
    for line in sudoku:
        if set(line) != true_set:
            return 0

    for line in zip(*sudoku):
        if set(line) != true_set:
            return 0

    for i in range(3):
        for j in range(3):
            block = set()
            for k in range(3):
                block.update(sudoku[3*i+k][3*j:3*j+3])
            if block != true_set:
                return 0
    return 1

T = int(input())
for test_case in range(1,1+T):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    print(f"#{test_case} {check_sudoku(sudoku)}")