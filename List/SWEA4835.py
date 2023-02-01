def my_max(*args):
    answer = args[0]
    for arg in args:
        if answer < arg:
            answer = arg
    return answer

def my_min(*args):
    answer = args[0]
    for arg in args:
        if answer > arg:
            answer = arg
    return answer

def my_sum(array):
    answer = 0
    for element in array:
        answer += element
    return answer

T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    Min,Max = float('inf'), float('-inf')
    for i in range(N-M+1):
        sub_sum = my_sum(arr[i:i + M])
        Min = my_min(Min,sub_sum)
        Max = my_max(Max,sub_sum)
    print(f"#{test_case} {Max-Min}")