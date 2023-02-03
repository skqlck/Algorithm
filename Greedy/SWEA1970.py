M = [50000,10000,5000,1000,500,100,50,10]
counts = [0,0,0,0,0,0,0,0]

T = int(input())
for test_case in range(1,1+T):
    money = int(input())
    for i in range(8):
        counts[i],money = divmod(money,M[i])
    print(f"#{test_case}")
    print(*counts)