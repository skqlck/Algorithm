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
DP[0] = A[0]
for i in range(1,N):
    DP[i] = max(DP[j] for j in range(i) if A[j]<A[i])+A[i]
print(max(DP))