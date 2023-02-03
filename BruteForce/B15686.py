"""
가능한 치킨집 조합을 뽑아서
집들의 치킨 거리 합의 최솟값을 출력하면 된다.
itertools.combinations를 사용해도 되고,
아래처럼 직접 만들어서 사용해도 된다.
각 집마다 치킨집까지의 거리를 미리 계산해놓고
후에 치킨집 조합에 따라 뽑아서 써도 된다. -> 이게 훨씬 빠르다. (치킨거리 계산을 딱 1번만 하기 때문)
"""
N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append([i,j])
        elif graph[i][j] == 1:
            houses.append([i,j])


def chicken_distance(chickens):
    global answer
    cd = 0 # chicken distance
    for house in houses:
        hcd = min([abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) for chicken in chickens])
        cd += hcd
        if answer <= cd:
            break
    else:
        answer = cd

def guzozojung(path,k): # 조합으로 치킨집을 뽑아야하므로, k를 활용
    if len(path) == M:
        return chicken_distance(path)
    for i in range(k,len(chickens)):
        chi_x,chi_y = chickens[i] # 치킨 행과 열 인덱스
        path.append([chi_x, chi_y])
        (path,i+1)
        path.pop()

answer = float('inf')
guzozojung([],0)
print(answer)

