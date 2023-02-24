from collections import deque
"""
Version 1
"""
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    queue = deque()
    visited = [0]*(10**6+1)
    visited[N] = 1
    queue.append((N,0))
    while queue:
        number,step = queue.popleft()
        if number == M:
            break
        if number+1 <= 1000000 and not visited[number+1]:
            queue.append((number+1,step+1))
            visited[number+1] = 1
        if 0 < number-1 <= 1000000 and not visited[number-1]:
            queue.append((number-1,step+1))
            visited[number-1] = 1
        if number <= 500000 and not visited[number*2]:
            queue.append((number*2,step+1))
            visited[number*2] = 1
        if 0 < number - 10 and not visited[number-10]:
            queue.append((number-10,step+1))
            visited[number-10] = 1
    print(f"#{test_case} {step}")
"""
Version 2
"""
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    queue = deque()
    visited = [0]*(10**6+1)
    visited[N] = 1
    queue.append(N)
    while queue:
        number= queue.popleft()
        step = visited[number]
        if number == M:
            break
        if number+1 <= 1000000 and not visited[number+1]:
            queue.append(number+1)
            visited[number+1] = step+1
        if 0 < number-1 <= 1000000 and not visited[number-1]:
            queue.append(number-1)
            visited[number-1] = step+1
        if number <= 500000 and not visited[number*2]:
            queue.append(number*2)
            visited[number*2] = step+1
        if 0 < number - 10 and not visited[number-10]:
            queue.append(number-10)
            visited[number-10] = step+1
    print(f"#{test_case} {visited[M]-1}")
