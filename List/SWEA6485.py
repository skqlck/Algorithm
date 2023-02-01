T = int(input())
for test_case in range(1,1+T):
    stations = [0]*5001
    for _ in range(int(input())):
        A,B = map(int,input().split())
        for station in range(A,B+1):
            stations[station] += 1
    answer = []
    for _ in range(int(input())):
        station = int(input())
        answer.append(stations[station])
    print(f"#{test_case} {' '.join(map(str,answer))}")