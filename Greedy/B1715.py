# import sys
# input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers = sorted(numbers)
answer = 0
for idx,number in enumerate(numbers):
    answer += (N-idx)*number
answer -= numbers[0]
print(answer)