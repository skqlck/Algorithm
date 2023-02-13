"""
집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
선형 시간에 정렬하는 효율적인 알고리즘

※제한사항
* 정수나 정수로 표현할 수 있는 자료에 대해서만 적용가능 (원소 값 자체가 인덱스이기 때문에)
* 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야한다.
"""

def Counting_Sort(A, k):
    counts = [0]*(k+1)
    B = [0]*(len(A))

    for a in A:
        counts[a] += 1

    for i in range(1,k+1):
        counts[i] += counts[i-1]

    for i in range(len(A)-1,-1,-1):
        counts[A[i]] -= 1
        B[counts[A[i]]] = A[i]
    return B

A = list(map(int,input().split()))
k = int(input())
print(Counting_Sort(A,k))