def Dec2Bin(value):
    s = ''
    while value > 1:
        s = str(value%2) + s
        value //= 2
    s = str(value)+s
    return s
def Hex2Dec(s):
    if s.isdigit():
        return int(s)
    return ord(s) - ord("A") + 10

T = int(input())
for test_case in range(1,1+T):
    N,Hex = input().split()
    N = int(N)
    answer = ''
    for num in Hex:
        bins = Dec2Bin(Hex2Dec(num))
        answer += '0'*(4-len(bins))+bins
    print(f"#{test_case} {answer}")