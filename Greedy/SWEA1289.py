# import sys
# sys.stdin = open('input.txt','r')
# T = int(input())
# for test_case in range(1,1+T):
#     bits = '0'+input()
#     cnt = 0
#     for i in range(len(bits)-1,0,-1):
#         if bits[i] != bits[i-1]:
#             cnt += 1
#     print(f"#{test_case} {cnt}")

T = int(input())
for test_case in range(1,1+T):
    now = 0
    bits = list(map(int,input()))
    cnt = 0
    for bit in bits:
        if bit != now:
            now = (now+1)%2
            cnt += 1
    print(f"#{test_case} {cnt}")