'''
조건 1. step은 1 또는 2
조건 2. 3개의 연속 계단X
조건 3. 마지막 계단은 무조건 밟아야한다.***

0번째와 1번째 계단은 당연하게 다 밟고 오는 것이 점수가 가장 크다

2번재의 경우 0번째를 밟으면 1번째를 밟으면 안되고,
            1번째를 밟고 오려면 0번째를 밟으면 안된다.
            (3칸 연속 X)

            ...

i번째 계단을 밟는 방법은 ***
    1. ... i-3 -> i-1 -> i (1칸 이동으로 온다면 3칸 연속을 고려)
    => DP[i-3] + stairs[i-1] + stairs[i]

    2. ... i-2 -> i (2칸 이동으로 온다면 3칸 연속을 고려X)
    => DP[i-2] + stairs[i]

DP[N-1]이 꼭 DP의 최대값은 아니다.
    [1,1,100,100,1] => DP = [1,2,101,201,103]
    마지막 칸을 무조건 밟아야하므로,
    마지막 칸을 밟았을 때의 최대값을 구해야한다.

'''
N = int(input())
stairs = [int(input()) for _ in range(N)]
if N <=2:
    print(sum(stairs))
else:
    DP = [0]*N
    DP[0] = stairs[0]
    DP[1] = stairs[0] + stairs[1]
    DP[2] = max(stairs[1]+stairs[2],stairs[0]+stairs[2])
    for i in range(3,N):
        DP[i] = max(DP[i-2],DP[i-3]+stairs[i-1]) + stairs[i]
    print(DP[N-1])


def add(n):
    if n<=1:
        return 1
    else:
        return add(n-1) + 1