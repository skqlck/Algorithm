import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,1+T):
    N,M = map(int,input().split())
    flag = False
    for _ in range(N):
        line = list(input().rstrip())
        if flag:
            continue
        for j in range(M-1,54,-1):
            if line[j] == "1":
                end = j
                start = j-55
                code = line[start:end+1]
                flag = True
                break
    Bits2Dec = {"0001101":0,
                "0011001":1,
                "0010011":2,
                "0111101":3,
                "0100011":4,
                "0110001":5,
                "0101111":6,
                "0111011":7,
                "0110111":8,
                "0001011":9}
    code2Dec = [0]*8
    for i in range(8):
        part = ''.join(code[7*i:7*i+7])
        code2Dec[i] = Bits2Dec[part]
    total = 0
    for i in range(4):
        total += 3*code2Dec[2*i]+code2Dec[2*i+1]
    if total%10 == 0:
        print(f"#{test_case} {sum(code2Dec)}")
    else:
        print(f"#{test_case} 0")



