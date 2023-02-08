import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    str1 = input()
    str2 = input()
    print(f"#{test_case} {1*(str1 in str2)}")