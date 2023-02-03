"""
카드 크기가 작은 순으로 합치는 것 O
단, 카드를 합치고 난 이후 새운 카드가 생기는데, 이것 또한 생각해야한다.
즉, 새로 합친 카드 묶음이 가장 작은 카드묶음이 아닐 수 있다.
50 60 70 80
 110
    180           -> 총 110+180+260 = 550
        260

50 60 70 80
 110   150        -> 총 110+150+260 = 520
    260
"""

# import sys
# input = sys.stdin.readline
import heapq

heap = []
N = int(input())
for i in range(N):
    heapq.heappush(heap, int(input()))
answer = 0
while len(heap) > 1:
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    answer += A+B
    if len(heap) == 0:
        break
    heapq.heappush(heap, A+B)
print(answer)

