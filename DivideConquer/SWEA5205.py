import sys
sys.stdin = open('input.txt')

def hoare(l,r):
    p = l
    lp = l
    rp = r
    while lp<=rp:
        while lp<=rp and lst[lp] <= lst[p]:
            lp += 1
        while lp<=rp and lst[rp] >= lst[p]:
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[p], lst[rp] = lst[rp], lst[p]

    return rp

def quicks(l,r):
    if l < r:
        p = hoare(l, r)
        quicks(l,p-1)
        quicks(p+1,r)

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    lst = list(map(int,input().split()))
    quicks(0, N - 1)
    print(f"#{test_case} {lst[N//2]}")