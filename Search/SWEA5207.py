import sys
sys.stdin = open('input.txt')
# ###################### Version 1 : BruteForce ######################
# def BS(start, end, dir, value):
#     global cnt
#     if start > end:
#         return
#
#     middle = (start + end) // 2
#     if A[middle] == value:
#         cnt += 1
#         return
#
#     if A[middle] < value:
#         if dir == 'right':
#             return
#         return BS(middle + 1, end, 'right', value)
#
#     if A[middle] > value:
#         if dir == 'left':
#             return
#         return BS(start, middle - 1, 'left', value)
#
#
# cnt = 0
# for value in B:
#     BS(0, N - 1, 'none', value)
# print(f"#{test_case} {cnt}")
# ####################################################################

# ###################### Version 2 : Memoization #####################
# def BS(start,end,dir):
#     if start > end:
#         return
#
#     if start == end:
#         Memoization[A[start]] = 1
#         return
#
#     middle = (start+end)//2
#     Memoization[A[middle]] = 1
#
#     if dir != 'right':
#         BS(middle+1,end,'right')
#
#     if dir != 'left':
#         BS(start,middle-1,'left')
#
# Memoization = [0] * (1000001)
# BS(0,N-1,'none')
# cnt = 0
# for value in B:
#     if Memoization[value]:
#         cnt += 1
# print(f"#{test_case} {cnt}")
# ####################################################################

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    ###################################
    ####### Select Ver1 or Ver2 #######
    ###################################