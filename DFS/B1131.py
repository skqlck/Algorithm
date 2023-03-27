A,B,K = map(int,input().split())
answer = 0

for i in range(A,B+1):
    DP = set()
    i = sorted(str(i))
    DP.add(i)
    while True:
        j = sum(map(lambda x:int(x)**K,i))
        if j == A:
            answer += A
            break
        j = sorted(str(i))
        if j in DP:
            answer += min(DP)
            break
        DP.add(j)
        i = j
print(answer)

