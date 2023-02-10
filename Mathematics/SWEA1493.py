import sys
sys.stdin = open("input.txt", "r")
def find_xy(n):
    level = int((2*n)**0.5)
    n -= int(level*(level-1)/2)
    while n - level > 0:
        n -= level
        level += 1
    return (1+(n-1),level-(n-1))

T = int(input())
for test_case in range(1,1+T):
    a,b = map(int,input().split())
    x1,y1 = find_xy(a)
    x2,y2 = find_xy(b)
    x,y = x1+x2,y1+y2
    level = x+y-1
    print(f"#{test_case} {int(level*(level-1)/2) + x}")
