import sys
sys.stdin = open("sample_input.txt","r")
def rotate(wheel, dir):
    if dir == 0:
        return wheel
    if dir == 1:
        return [wheel[7]] + wheel[:7]
    if dir == -1:
        return wheel[1:] + [wheel[0]]

T = int(input())
for test_case in range(1,1+T):
    K = int(input())
    wheels = []
    for _ in range(4):
        wheels.append(list(map(int,input().split())))

    for _ in range(K):
        num, rotate_direction = map(int,input().split())
        num -= 1 # 바퀴 인덱스는 0부터!!
        wheel_rotate = [0,0,0,0]
        wheel_rotate[num] = rotate_direction
        for left in range(num-1,-1,-1):
            if wheels[left+1][6] != wheels[left][2]:
                wheel_rotate[left] = -wheel_rotate[left+1]
        for right in range(num+1,4):
            if wheels[right-1][2] != wheels[right][6]:
                wheel_rotate[right] = -wheel_rotate[right-1]

        for i in range(4):
            wheels[i] = rotate(wheels[i],wheel_rotate[i])

    total_score = 0
    for i in range(4):
        total_score += 2**i*wheels[i][0]
    print(f"#{test_case} {total_score}")