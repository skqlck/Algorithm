T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    bottom,top = 1,10**6
    while bottom <= top:
        mid = (bottom + top) // 2
        if mid**3 == N:
            print(f"#{test_case} {mid}")
            break
        elif mid**3 > N:
            top = mid-1
        else:
            bottom = mid+1
    else:
        print(f"#{test_case} -1")