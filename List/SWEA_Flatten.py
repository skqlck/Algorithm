"""
가로 길이 항상 100
높이는 항상 1이상 100이하
덤프 횟수 1이상 1000이하
높이 차를 항상 구한다 O(dump횟수)
        덤프가 전부 끝난 후 구한다. O(1) 채택! (최저점과 최고점은 항상 기억)
"""
import sys
sys.stdin = open('List/input.txt','r')
for test_case in range(1,11):
    dump = int(input())
    heights = [0]*101
    lowest,highest = 100,0
    for height in map(int,input().split()):
        heights[height] += 1
        if height > highest:
            highest = height
        elif height < lowest:
            lowest = height

    for _ in range(dump):
        heights[highest] -= 1
        heights[highest-1] += 1
        if heights[highest] == 0:
            highest -= 1

        heights[lowest] -= 1
        heights[lowest+1] += 1
        if heights[lowest] == 0:
            lowest += 1

        if highest == lowest:
            break

    print(f"#{test_case} {highest-lowest}")