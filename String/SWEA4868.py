import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    char_dict = {}
    for char in input():
        char_dict[char] = 0
    for char in input():
        if char in char_dict:
            char_dict[char] += 1
    answer = 0
    for value in char_dict.values():
        if value > answer:
            answer = value
    print(f"#{test_case} {answer}")