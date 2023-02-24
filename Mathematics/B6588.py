DP = [0,0,1]+[1,0]*500000
DP[0] = 0
DP[1] = 0
for i in range(3,1000000,2):
    if DP[i]:
        for j in range(2*i,1000000,i):
            DP[j] = 0
N = int(input())
while N != 0:
    for a in range(3,N,2):
        if DP[a] and DP[N-a]:
            print(f"{N} = {a} + {N-a}")
            break
    N = int(input())