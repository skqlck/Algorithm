import sys
sys.stdin = open("input.txt", "r")
"""
큐에 들어갈 원소 수와 순서가 항상 정해졌으므로, 그냥 리스트로 사용하자
collections.deque()를 사용하면 빠르긴하지만 메소드를 부르는 과정때문에 역으로 느려질 수도 있다.
더 정확히 말하자면, 큐가 필요가 없는 문제
"""
for test_case in range(1,11):
    input()
    graph = [list(map(int,input().split())) for _ in range(100)]
    """
    visited = [[0 for _ in range(100)] for _ in range(100)]
    ※ 방문처리하면 큰일남! (노선이 겹칠 수 있어서 한놈이 딴놈을 막을수도)
    
    진행방향 
    * 0이면 위에서 아래로
    * 1이면 왼쪽에서 오른쪽으로
    *-1이면 오른쪽에서 왼쪽으로
    """
    queue = []
    num_of_start = 0
    for y in range(100):
        if graph[0][y]:
            queue.append((0,y,0,y)) # x,y, 진행방향, 시작점
            num_of_start += 1
    def main():
        while True:
            for i in range(num_of_start):
                x,y,d,start = queue[i]
                if x == 99:
                    print(f"#{test_case} {start}")
                    return

                if y-1 > -1 and graph[x][y-1] and d != 1:
                    queue[i] = (x,y-1,-1,start)
                elif y+1 < 100 and graph[x][y+1] and d != -1:
                    queue[i] = (x,y+1,1,start)
                else:
                    queue[i] = (x+1,y,0,start)
    main()