def my_max(arg1, *args):
    if not args:
        args = arg1
    else:
        return my_max(args+(arg1,))

    answer = args[0]
    for arg in args:
        if answer < arg:
            answer = arg
    return answer

def my_min(arg1, *args):
    if not args:
        args = arg1
    else:
        return my_min(args+(arg1,))

    answer = args[0]
    for arg in args:
        if answer > arg:
            answer = arg
    return answer

T = int(input())
for test_case in range(1,1+T):
    input()
    array = list(map(int,input().split()))
    print(f"#{test_case} {my_max(array)-my_min(array)}")