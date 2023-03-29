import sys
sys.stdin = open('input.txt')
def N2Dec(num, N):
    n = len(num)
    answer = 0
    for i in range(n):
        if num[i] != '0':
            answer += int(num[i])*N**(n-1-i)
    return answer

T = int(input())
for test_case in range(1,1+T):
    bin = input()
    ter = input()
    bin2Dec = N2Dec(bin,2)
    db = len(bin)
    dt = len(ter)
    ter2Dec = N2Dec(ter,3)
    flag = False
    for i in range(db):
        if bin[i] == '1':
            bin_temp = bin2Dec - 2**(db-1-i)
        else:
            bin_temp = bin2Dec + 2**(db-1-i)
        for j in range(dt):
            gap = 3 ** (dt - 1 - j)
            if ter[j] == '0':
                if bin_temp == ter2Dec + gap:
                    flag = True
                    break
                if bin_temp == ter2Dec + 2*gap:
                    flag = True
                    break
            elif ter[j] == '1':
                if bin_temp == ter2Dec - gap:
                    flag = True
                    break
                if bin_temp == ter2Dec + gap:
                    flag = True
                    break
            else:
                if bin_temp == ter2Dec - gap:
                    flag = True
                    break
                if bin_temp == ter2Dec -2*gap:
                    flag = True
                    break
        if flag:
            print(f"#{test_case} {bin_temp}")
            break