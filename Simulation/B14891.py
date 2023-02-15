wheels = []
for _ in range(4):
    wheels.append(list(map(int,input())))
K = int(input())
for k in range(K):
    orders = []
    n,d = map(int,input().split())
    ld,rd = d,d
    n -= 1 # 바퀴 번호는 0번부터 시작
    orders.append([n,d])
    for l in range(n-1,-1,-1):
        if wheels[l][2] != wheels[l+1][6]:
            ld *= -1
            orders.append([l,ld])
        else:
            break
    for r in range(n+1,4):
        if wheels[r-1][2] != wheels[r][6]:
            rd *= -1
            orders.append([r,rd])
        else:
            break
    for nd in orders:
        n,d = nd
        if d == 1:
            wheels[n] = [wheels[n][-1]]+wheels[n][:-1]
        else:
            wheels[n] = wheels[n][1:]+[wheels[n][0]]
total_score = 0
for i in range(4):
    total_score += wheels[i][0]*(2**i)
print(total_score)