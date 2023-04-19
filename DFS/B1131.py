A,B,K = map(int,input().split())
power = [i**K for i in range(10)]
DP = [0]*(3188647)
def getNextSeq(number):
    return sum(map(lambda x: power[int(x)], str(number)))

answer = 0
for number in range(A,B+1):
    if not DP[number]:
        path = {}
        path[number] = 1
        now = number
        while True:

            next = getNextSeq(now)

            if DP[next]: # 기존 방문한 것들과 만남
                minV = DP[next]
                list_path = list(path.keys())
                for idx in range(-1,-len(path)-1,-1):
                    before = list_path[idx]
                    if before < minV:
                        minV = before
                    DP[before] = minV
                break

            if next in path: # 사이클 형성
                list_path = list(path.keys())
                Cycle = set()
                Cycle.add(next)
                CycleMinV = next
                while True:
                    next = getNextSeq(next)
                    if next in Cycle:
                        break
                    Cycle.add(next)
                    if next < CycleMinV:
                        CycleMinV = next

                for node in Cycle:
                    DP[node] = CycleMinV

                for idx in range(len(list_path) - len(Cycle) - 1,-1,-1):
                    if list_path[idx] < CycleMinV:
                        CycleMinV = list_path[idx]
                    DP[list_path[idx]] = CycleMinV
                break
            # visited[next] = 1
            path[next] = 1
            now = next

    answer += DP[number]

print(answer)