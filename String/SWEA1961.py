def rotate90(array):
    return [list(row[::-1]) for row in zip(*array)]

import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    degree_90 = rotate90(array)
    degree_180 = rotate90(degree_90)
    degree_270 = rotate90(degree_180)
    print(f"#{test_case}")
    for i in range(N):
        print(''.join(map(str,degree_90[i])),''.join(map(str,degree_180[i])),''.join(map(str,degree_270[i])))