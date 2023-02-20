import sys
sys.stdin = open("input.txt","r")
for test_case in range(1,11):
    input()
    arr = list(map(int,input().split()))
    num = 1
    flag = True
    while flag:
        for i in range(1,6):
            new = arr.pop(0)-i
            if new <= 0:
                arr.append(0)
                print("#" + str(test_case), *arr)
                flag = False
                break
            arr.append(new)
