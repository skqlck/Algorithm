"""
* 첫 번째 원소부터 인접한 원소끼리
  계속 자리를 교환하면서
  맨 마지막 자리까지 이동
* 한 단계가 끝나면
  가장 큰 원소가 마지막 자리로 정렬

교환하며 자리를 이동하는 모습이
물 위에 올라오는 거품 모양과 같다고 하여
버블 정렬이라고 한다.
Time Complexity : O(n^2)
"""
A = list(map(int, input().split()))
for i in range(len(A)-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print(*A)
print(A == sorted(A))
