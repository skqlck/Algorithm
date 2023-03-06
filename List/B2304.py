heights = [1001]*1000
blocks = [0]*1000
for _ in range(int(input())):
    L,H = map(int,input().split())
    blocks[L-1] = H
local_max = blocks[0]
for i in range(1000):
    if blocks[i] > local_max:
        local_max = blocks[i]
    heights[i] = min(heights[i],local_max)
local_max = blocks[-1]
for i in range(999,-1,-1):
    if blocks[i] > local_max:
        local_max = blocks[i]
    heights[i] = min(heights[i],local_max)
answer = 0
for height in heights:
    if height != 1001:
        answer += height
print(answer)