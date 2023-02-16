def RSP(i,j):
    if arr[i] == arr[j]:
        if i < j:
            return i
        return j

    if arr[i]+arr[j] == 4:
        if arr[i] == 1:
            return i
        return j

    if arr[i] > arr[j]:
        return i
    return j

def DnQ(i,j):
    if i == j:
        return i
    if i + 1 == j:
        return RSP(i,j)
    return RSP(DnQ(i,(i+j)//2),DnQ((i+j)//2+1,j))

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{test_case} {DnQ(0,N-1)+1}")