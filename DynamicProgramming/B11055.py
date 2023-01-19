'''
DP[i]의 값은 부분 수열의 가장 큰 값이 A[i]인 수열의 합!
만약, DP[i-1]까지 최적해를 구했다면 DP[i]는
(j < i) & (A[j]<A[i]) 인 j들 중에서 DP[j]+A[i] 중 최대값
즉, 현재 값(A[i])보다 앞선 원소 중(j<i)에서 작은 값(A[j]<A[i]).
그 작은 값의 DP값 중(DP[j_1],DP[j_2],...) 최대값이
현재 DP[i]의 앞부분!
'''
N = int(input())
A = list(map(int,input().split()))
DP = [0 for _ in range(N)]
DP[:] = A[:]
'''
DP의 초기값을 A와 같게 설정하는 이유?
초기값 -> A = [100,10,91], DP = [100,0,0] 으로 설정
i == 1 -> DP = [10000,0,0]
i == 2 -> DP = [10000,0,91]
DP의 초기값이 0이므로 후에 부분수열에서 해당 원소를 포함하지 않는 것처럼 됨 
'''
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[j]+A[i],DP[i])
print(max(DP))