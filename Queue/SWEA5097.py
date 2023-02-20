for test_case in range(1,int(input())+1):
    N,M = map(int,input().split())
    print(f"#{test_case} {input().split()[M%N]}")