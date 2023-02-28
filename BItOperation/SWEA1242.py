import sys
sys.stdin = open("sample_input.txt","r")

Hex2Bin = {"0":"0000",
           "1":"0001",
           "2":"0010",
           "3":"0011",
           "4":"0100",
           "5":"0101",
           "6":"0110",
           "7":"0111",
           "8":"1000",
           "9":"1001",
           "A":"1010",
           "B":"1011",
           "C":"1100",
           "D":"1101",
           "E":"1110",
           "F":"1111"}

Bits2Dec = {211:"0",
            221:"1",
            122:"2",
            411:"3",
            132:"4",
            231:"5",
            114:"6",
            312:"7",
            213:"8",
            112:"9"}

T = int(input())
for test_case in range(1,1+T):
    answer = 0
    N,M = map(int,input().split())
    codes = [list(input().rstrip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            codes[i][j] = Hex2Bin[codes[i][j]]
        codes[i] = ''.join(codes[i])

    for row in range(1,N):
        col = M*4-1
        while col > 54:
            if codes[row][col] == "1" and codes[row-1][col] == "0":
                one_line = [-1] * 8
                for idx in range(8):
                    cnt1 = 0
                    while codes[row][col] == "1":
                        cnt1 += 1
                        col -= 1

                    cnt2 = 0
                    while codes[row][col] == "0":
                        cnt2 += 1
                        col -= 1

                    cnt3 = 0
                    while codes[row][col] == "1":
                        cnt3 += 1
                        col -= 1

                    while codes[row][col] == "0":
                        col -= 1

                    ratio = min(cnt1,cnt2,cnt3)
                    code = Bits2Dec[(cnt3*100+cnt2*10+cnt1)//ratio]
                    one_line[7-idx] = code

                total = int(one_line[7])
                for i in range(7):
                    if i % 2 == 0:
                        total += 3 * int(one_line[i])
                    else:
                        total += int(one_line[i])
                if total % 10 == 0:
                    answer += sum(map(int,one_line))
            else:
                col -= 1
    print(f"#{test_case} {answer}")