T = int(input())
for test_case in range(1,1+T):
    result = ''
    total = 0
    for _ in range(int(input())):
        char,num = input().split()
        result += char*int(num)
        total += int(num)
    print(f"#{test_case}")
    for i in range(total//10+1):
        print(result[10*i:10*(i+1)])
