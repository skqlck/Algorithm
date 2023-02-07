T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    A = list(map(int,input().split()))
    # 선택 정렬을 이용해서
    for i in range(N-1):
        idx = i
        if i % 2:
            # 홀수 인덱스는 최소값 찾기
            for j in range(i+1,N):
                if A[idx] > A[j]:
                    idx = j
        else:
            # 짝수 인덱스는 최대값 찾기
            for j in range(i+1,N):
                if A[idx] < A[j]:
                    idx = j
        A[i],A[idx] = A[idx],A[i]
    print(f"#{test_case} {' '.join(map(str,A[:10]))}")
