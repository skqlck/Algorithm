import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,1+T):
    N,M,K = map(int,input().split())
    customers = [0]*11112
    for customer in list(map(int,input().split())):
        customers[customer] += 1

    boong = 0
    for i in range(0,11112,M):
        num_of_customers = sum(customers[i:i+M])
        if num_of_customers > boong:
            print(f"#{test_case} Impossible")
            break
        boong -= num_of_customers
        boong += K
    else:
        print(f"#{test_case} Possible")
