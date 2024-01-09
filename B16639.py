import sys
from pprint import pprint as print
sys.stdin = open('B16639.txt')
input = sys.stdin.readline

N = int(input())
expression = input()
numbers = []
operations = []
for i in range(N):
    if i%2 == 0:
        numbers.append(int(expression[i]))
    else:
        operations.append(expression[i])

MinMax = [[[0,0] for _ in range(N//2+1)] for _ in range(N//2+1)]

def getMinMax(x,y):
    if x==y:
        return numbers[x], numbers[x]
    
    values = []
    for mid in range(x,y):
        values.append(calculate(MinMax[x][mid][0],MinMax[mid+1][y][0],operations[mid]))
        values.append(calculate(MinMax[x][mid][0],MinMax[mid+1][y][1],operations[mid]))
        values.append(calculate(MinMax[x][mid][1],MinMax[mid+1][y][0],operations[mid]))
        values.append(calculate(MinMax[x][mid][1],MinMax[mid+1][y][1],operations[mid]))
    return min(values), max(values)

def calculate(a,b,operation):
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    else:
        print('잘못된 연산자')
        return
    

for step in range(N//2+1):
    x,y = 0,step
    for i in range(N//2+1-step):
        nx,ny = x+i,y+i
        minV,maxV = getMinMax(nx,ny)
        MinMax[nx][ny][0] = minV
        MinMax[nx][ny][1] = maxV

print(MinMax[0][N//2][1])