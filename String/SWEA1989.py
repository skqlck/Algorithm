T = int(input())
for test_case in range(1,1+T):
    word = input()
    print(f"#{test_case} {1*(word == word[::-1])}")