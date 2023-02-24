T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    heap = [0]*(N+1)
    last = 0
    for value in map(int,input().split()):
        last += 1
        heap[last] = value
        c = last
        p = last//2
        while p > 0 and heap[p] > heap[c]:
            heap[p],heap[c] = heap[c],heap[p]
            c = p
            p = c//2

    answer = 0
    node = N//2
    while node:
        answer += heap[node]
        node //= 2
    print(f"#{test_case} {answer}")