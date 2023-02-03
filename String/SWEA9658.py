T = int(input())
for test_case in range(1,1+T):
    num = input()
    num = str(round(int(num),-len(num)+2))
    print(f"#{test_case} {'.'.join(num[:2])}*10^{len(num)-1}")