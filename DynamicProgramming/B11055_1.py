'''
1<= N <=1000
1<= A_i <= 1000 
DP[a]는 부분 수열의 마지막 값이 a인 부분 수열의 합의 최대값
A의 원소들을 순회하면서, 현재 원소가 a일때 
a보다 작은 원소들(i<a)에 대해서
DP[a] = max(DP[i] for i in range(1,a)) + a
※ a는 인덱스라기보단 A의 원소 ※
'''
N = int(input())
A = list(map(int,input().split()))
DP = [0 for _ in range(1001)]
for a in A:
    DP[a] = max(DP[:a]) + a
print(max(DP))