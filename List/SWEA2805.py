def my_sum(Iterable):
    total = 0
    for element in Iterable:
        total += element
    return total

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]
    earn = 0

    for i in range(N//2):
        earn += my_sum(graph[i][N//2-i:N//2+i+1])
        earn += my_sum(graph[-i-1][N//2-i:N//2+i+1])
    earn += my_sum(graph[N//2])

    print(f"#{test_case} {earn}")