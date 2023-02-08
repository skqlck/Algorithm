import sys
sys.stdin = open("GNS_test_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N = int(input().split()[1])
    numbers = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for number in input().split():
        numbers[number] += 1
    print(f"#{test_case}")
    for key,value in numbers.items():
        print((key+' ')*value, end=' ')
    print()
