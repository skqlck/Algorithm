"""
N개 쌓는 방법은
N-1개 쌓는 방법에서 가로 타일 세우고
               +
N-2개 쌓는 방법에서 세로 타일 세우기
"""
n = int(input())
DP = [0]*1001
DP[1] = 1
DP[2] = 2
for i in range(3, n+1):
    DP[i] = (DP[i-1]+DP[i-2]) % 10007
print(DP[n])