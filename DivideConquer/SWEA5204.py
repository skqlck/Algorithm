import sys
sys.stdin = open('input.txt','r')

def merge(left, right):
    global cnt
    result = []

    lp = 0
    rp = 0
    if left[-1] > right[-1]:
        cnt += 1
    while lp<len(left) and rp<len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    result.extend(left[lp:])
    result.extend(right[rp:])

    return result

def mergeSort(lst):
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = lst[:m]
    right = lst[m:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    lst = mergeSort(lst)
    print(f"#{test_case} {lst[N//2]} {cnt} ")
