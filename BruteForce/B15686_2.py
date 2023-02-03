"""
Using itertools.combinations
"""
# import sys
# input =sys.stdin.readline
from itertools import combinations
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
chickens = []
homes = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append([i,j])
        elif graph[i][j] == 1:
            homes.append([i,j])

def get_chicken_distance(homes,chickens):
    global answer
    cd = 0
    for home in homes:
        hcd = min([abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]) for chicken in chickens])
        cd += hcd
        if cd >= answer:
            break
    else:
        answer = cd
answer = 2*N*M*100
for chickens_combi in combinations(chickens,M):
    get_chicken_distance(homes,chickens_combi)

print(answer)