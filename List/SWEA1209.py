# import sys
# sys.stdin = open('input.txt','r')
for test_case in range(1,11):
    T = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    row = max(map(sum,array))
    L2R = sum(array[i][i] for i in range(100))
    R2L = sum(array[i][99-i] for i in range(100))
    col = max(map(sum,map(list,zip(*array))))
    print(f"#{test_case} {max([row,col,L2R,R2L])}")