"""
1. 스택을 사용할 수 있지만, 스택을 사용하면 메모리 초과
-> 스택의 구조를 사용하지만, 스택은 사용하지 않는 느낌

2. 가격의 최대값을 N-1번째 가격이라고 하고,
   N-2번째부터 0번째까지 가격을 확인하면,
   만약 i(0 <= i <= N-2)번째 가격이 가격의 최대값보다 작으면
   가격의 최대값이 팔고
   만약 i(0 <= i <= N-2)번째 가격이 가격의 최대값보다 크다면
   가격의 최대값은 i번째 가격이 된다.
   이때, 새로운 최대 가격에 기존 최대 가격의 상품을 팔 수 있을까? X
   => 미래에서부터 과거로(N-1부터 0d으로) 오기 때문에, 파는 것은
      미래의 가격에 팔 수 있지, 과거의 가격에 팔 수 없다.

3. 미래에서부터 과거로 오면 O(N)
   과거부터 미래로 오면 O(N^2)
"""

T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    local_max = 0
    for i in range(N-1, -1, -1):
        if prices[i] < local_max:
            total += local_max - prices[i]
        else:
            local_max = prices[i]
    print(f'#{test_case} {total}')
